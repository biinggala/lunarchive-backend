import client from "../../client";
import { protectedResolver } from "../../users/users.utils";

export default {
  Mutation: {
    readMessage: protectedResolver(async (_, { id }, { loggedInUser }) => {
      const message = await client.message.findFirst({
        where: {
          id, //메시지 id
          userId: { not: loggedInUser.id }, //상대가 보낸 메시지
          room: { users: { some: { id: loggedInUser.id } } }, //내가 그 방에 있어야 함
        },
        select: { id: true },
      });
      if (!message) {
        return {
          ok: false,
          error: "Message not found.",
        };
      }
      await client.message.update({
        where: { id },
        data: {
          read: true,
        },
      });
      return {
        ok: true,
      };
    }),
  },
};
