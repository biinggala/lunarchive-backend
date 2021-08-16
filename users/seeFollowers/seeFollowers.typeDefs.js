import { gql } from "apollo-server";

export default gql`
  type seeFollowersResult {
    ok: Boolean!
    error: String
    followers: [User]
    totalPages: Int!
  }
  type Query {
    seeFollowers(username: String!, lastId: Int): seeFollowersResult!
  }
`;
