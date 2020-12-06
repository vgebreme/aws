SOLUTION

	You cannot just copy and paste this solution code because
	the bucket name needs to be your bucket name.

	If you run it "as is" it will not work!

	You must replace <FMI> with your bucket name.

	E.g.,

	2019-03-02-sally-catlostandfoundwebsite

	Keep the quotes around the bucket name, and  only
	replace the characters <FMI>.

'''
import boto3
S3API=boto3.client("s3", region_name="us-east-1")
bucket_name="<FMI>"
file_path="/home/ec2-user/environment/resources/"
file_name="config.js"
S3API.upload_file(file_path + file_name, bucket_name, file_name, ExtraArgs={"ContentType": "text/javascript", "CacheControl": "max-age=0"})
