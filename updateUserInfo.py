import json
import boto3
import datetime

s3 = boto3.client('s3')

BUCKET_NAME = 'getfitdatabase-339713187152-us-east-2-an'  # Replace with your S3 bucket name

def lambda_handler(event, context):

    raw_body = event.get('body') or '{}'
    try:
        request_body = json.loads(raw_body) if isinstance(raw_body, str) else raw_body
    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "Request body must be valid JSON"})
        }

    username = request_body.get("username") if isinstance(request_body, dict) else None
    if not isinstance(username, str) or not username.strip():
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "A non-empty username is required"})
        }

    newData = request_body.get("newData") if isinstance(request_body, dict) else None
    if not isinstance(username, str) or not username.strip():
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "A non-empty newData is required"})
        }



    object_key = f"users/{username}.json"
    response = s3.get_object(Bucket=BUCKET_NAME, Key=object_key)
    data = json.loads(response['Body'].read())
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=object_key,
        Body= json.dumps(newData)
    )
    # 
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(
            {
                "message": "User info updated successfully",
                "given": request_body
            }
        )
    }
