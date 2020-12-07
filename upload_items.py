
import boto3
S3API=boto3.client("s3", region_name="us-east-1")
bucket_name="bucketname"
file_path="/home/ec2-user/environment"
file_name="config.js"
S3API.upload_file(file_path + file_name, bucket_name, file_name, ExtraArgs={"ContentType": "text/javascript", "CacheControl": "max-age=0"})
