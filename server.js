require("dotenv").config();
import express from "express";
import logger from "morgan";
import { ApolloServer } from "apollo-server-express";
import { ApolloServerPluginLandingPageGraphQLPlayground } from "apollo-server-core";
import { typeDefs, resolvers } from "./schema";
import { getUser } from "./users/users.utils";
import { graphqlUploadExpress } from "graphql-upload";

const PORT = process.env.PORT;

const app = express();
const startServer = async () => {
  const apollo = new ApolloServer({
    resolvers,
    typeDefs,
    context: async ({ req }) => {
      return {
        loggedInUser: await getUser(req.headers.token),
      };
    },
    plugins: [ApolloServerPluginLandingPageGraphQLPlayground()],
  });

  await apollo.start();

  app.use(logger("tiny"));
  app.use(graphqlUploadExpress());
  app.use("/static", express.static("uploads"));
  apollo.applyMiddleware({ app });

  await new Promise((r) => app.listen({ port: PORT }, r)).then(() =>
    console.log(
      `🚀 Server is running on http://localhost:${PORT}${apollo.graphqlPath} ✅`
    )
  );
};
startServer();
