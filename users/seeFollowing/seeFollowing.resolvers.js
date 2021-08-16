import client from "../../client";

export default {
  Query: {
    seeFollowing: async (_, { username, lastId }) => {
      const checkUser = await client.user.findUnique({
        where: { username },
        select: { id: true },
      });
      if (!checkUser) {
        return {
          ok: false,
          error: "User not found.",
        };
      }
      const following = await client.user
        .findUnique({ where: { username } })
        .following({
          take: 10,
          skip: lastId ? 1 : 0,
          ...(lastId && { cursor: { id: lastId } }),
        });

      return {
        ok: true,
        following,
      };
    },
  },
};
