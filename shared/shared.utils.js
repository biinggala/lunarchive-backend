import AWS from "aws-sdk";

AWS.config.update({
  credentials: {
    accessKeyId: process.env.AWS_KEY,
    secretAccessKey: process.env.AWS_SECRET,
  },
  region: "ap-northeast-2",
});

const bucket = "instaclone--uploadss";

export const uploadToS3 = async (file, userId, folderName) => {
  const { filename, createReadStream } = await file;
  const readStream = createReadStream();
  const objectName = `${folderName}/${userId}-${Date.now()}-${filename}`;
  const { Location } = await new AWS.S3()
    .upload({
      Bucket: bucket,
      Key: objectName,
      ACL: "public-read",
      Body: readStream,
    })
    .promise();
  return Location;
};

export const delPhotoS3 = async (fileUrl, folderName) => {
  const filePath = fileUrl.split("/uploads/")[1]; // 파일명만 split 후 선택
  const params = {
    Bucket: `${bucket}/${folderName}`, // Bucket에 폴더 명 uploads 추가
    Key: filePath,
  };
  await new AWS.S3()
    .deleteObject(params, (error, data) => {
      if (error) {
        console.log(error);
      } else {
        console.log(data);
      }
    })
    .promise();
};
