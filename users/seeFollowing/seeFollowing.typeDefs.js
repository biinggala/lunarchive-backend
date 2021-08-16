import { gql } from "apollo-server";

export default gql`
  type seeFollowingResult {
    ok: Boolean!
    error: String
    following: [User]
    totalPages: Int!
  }
  type Query {
    seeFollowing(username: String!, lastId: Int): seeFollowingResult!
  }
`;
