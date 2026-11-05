import json
import boto3

s3 = boto3.client('s3')

BUCKET_NAME = 'getfitdatabase-339713187152-us-east-2-an'

def lambda_handler(event, context):

    request_body = json.loads(event.get('body') or '{}')

    username = request_body.get("username")
    index = request_body.get("index")
    updateWorkout = request_body.get("workout")

    object_key = f"users/{username}.json"

    response = s3.get_object(Bucket=BUCKET_NAME, Key=object_key)
    data = json.loads(response['Body'].read())

    if index is None or not isinstance(index, int) or index < 0 or index >= len(data["logHistory"]):
        return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"message": "Invalid workout index"})
        }

    data["logHistory"][index].update(updateWorkout)

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=object_key,
        Body=json.dumps(data)
    )

    return {
    "statusCode": 200,
    "headers": {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
    },
    "body": json.dumps(data)
}