import boto3, sys

DYNAMODB_CLIENT = boto3.client("dynamodb", region_name="us-east-1")

def my_init(event):
    if (event == None):
        breed=sys.argv[1]
    else:
        breed=event["breed_str"]
    if (breed=="All"):
        return scanTable()
    else:
        return queryIndex(breed)

def queryIndex(breed):
    response = DYNAMODB_CLIENT.query(
        TableName="lostdogs",
        IndexName="breed_index",
        ExpressionAttributeValues={":breed":{"S":breed}},
        KeyConditionExpression="breed = :breed"
    )
    print(response["Items"]) # for testing in Cloud9 console
    return response["Items"]

def scanTable():
    response = DYNAMODB_CLIENT.scan(
        TableName="lostdogs"
    )
    print(response["Items"]) # for testing in Cloud9 console
    return response["Items"]


def handler(event, context):
    print("Running as a script in Lambda")
    return my_init(event)

if __name__ == "__main__":
    print("Running as a script in Cloud9")
    my_init(None)