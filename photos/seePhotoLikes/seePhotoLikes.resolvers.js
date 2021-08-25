import client from "../../client";

export default {
  Query: {
    seePhotoLikes: async (_, { photoId, lastId }) => {
      const likedUser = await client.like.findMany({
        where: { photoId },
        select: {
          id: true,
          user: true,
        },
        take: 10,
        skip: lastId ? 1 : 0,
        ...(lastId && { cursor: { id: lastId } }),
      });
      return likedUser.map((like) => like.user);
    },
  },
};
