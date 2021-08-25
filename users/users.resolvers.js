import client from "../client";

export default {
  User: {
    totalFollowing: ({ id }) => {
      return client.user.count({
        where: { followers: { some: { id } } },
      });
    },
    totalFollowers: ({ id }) => {
      return client.user.count({
        where: { following: { some: { id } } },
      });
    },
    isMe: ({ id }, _, { loggedInUser }) => {
      return id === loggedInUser?.id;
    },
    isFollowing: async ({ id, isMe }, _, { loggedInUser }) => {
      if (!loggedInUser || isMe) {
        return false;
      }
      const checkFollowing = await client.user.count({
        where: { username: loggedInUser.username, following: { some: { id } } },
      });
      return Boolean(checkFollowing);
    },
    photos: ({ id }, { lastId }) =>
      client.user
        .findUnique({ where: { id } })
        .photos({
          take: 15,
          skip: lastId ? 1 : 0,
          ...(lastId && { cursor: { id: lastId } }),
        }),
  },
};
