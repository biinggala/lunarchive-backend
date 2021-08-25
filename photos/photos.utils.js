export const processHashtags = (caption) => {
  const hashtags = caption.match(/#[ㄱ-ㅎ|ㅏ-ㅣ|가-힣|\w]+/g) || [];
  return hashtags.map((hashtag) => ({
    where: { hashtag },
    create: { hashtag },
  }));
};

export const cursorPagination = (lastId) => {
  return {
    take: 15,
    skip: lastId ? 1 : 0,
    ...(lastId && { cursor: { id: lastId } }),
  };
};
