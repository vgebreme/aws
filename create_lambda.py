import boto3

LAMBDA_CLIENT = boto3.client("lambda")

result = LAMBDA_CLIENT.create_function(
    Code={"S3Bucket": "<FMI>","S3Key": "website_api_code.zip"},
    Description="Amazing cat website",
    FunctionName="CatSearch",
    Handler="query_cats.handler",
    MemorySize=128,
    Publish=True,
    Role="<FMI>",
   	Runtime="python3.6",
   	Timeout=30
)
print(result)