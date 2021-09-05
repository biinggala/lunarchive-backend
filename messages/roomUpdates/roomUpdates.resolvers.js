import { withFilter } from "graphql-subscriptions";
import client from "../../client";
import { NEW_MESSAGE } from "../../constants";
import pubsub from "../../pubsub";

export default {
  Subscription: {
    roomUpdates: {
      subscribe: async (root, args, context, info) => {
        const room = await client.room.findFirst({
          where: {
            id: args.id, //room id가 일치하는가
            users: { some: { id: context.loggedInUser.id } }, //해당 id의 유저가 속한 방인가
          },
          select: { id: true },
        });
        if (!room) {
          throw new Error("You can't enter this room.");
        }
        return withFilter(
          () => pubsub.asyncIterator(NEW_MESSAGE),
          async ({ roomUpdates }, { id }, { loggedInUser }) => {
            if (roomUpdates.roomId === id) {
              const room = await client.room.findFirst({
                where: {
                  id, //room id가 일치하는가
                  users: { some: { id: loggedInUser.id } }, //해당 id의 유저가 속한 방인가
                },
                select: { id: true },
              });
              if (!room) {
                return false;
              }
              return true;
            }
          }
        )(root, args, context, info);
      },
    },
  },
};
