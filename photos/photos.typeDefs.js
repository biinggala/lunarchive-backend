import { gql } from "apollo-server";

export default gql`
  type Photo {
    id: Int!
    user: User!
    file: String!
    caption: String
    likes: Int!
    hashtags: [Hashtag]
    comments: Int!
    createdAt: String!
    updatedAt: String!
    isMine: Boolean!
  }
  type Hashtag {
    id: Int!
    hashtag: String!
    photos(lastId: Int): [Photo]
    totalPhotos: Int!
    createdAt: String!
    updatedAt: String!
  }
  type Like {
    id: Int!
    photo: Photo!
    createdAt: String!
    updatedAt: String!
  }
`;
