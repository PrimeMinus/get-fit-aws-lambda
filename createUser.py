import json
import boto3
import datetime

s3 = boto3.client('s3')

BUCKET_NAME = 'getfitdatabase-339713187152-us-east-2-an'

def lambda_handler(event, context):
    # Extract request info
    http_method = event.get('httpMethod') or event.get('requestContext', {}).get('http', {}).get('method', 'UNKNOWN')
    path = event.get('path') or event.get('rawPath', '/')
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

    body = {
        "plan": {
            "startDate": "",
            "goalWeight": 0,
            "startWeight": 0,
            "finishDate": ""
        },
        "data": {
            "currentWeight": 0,
            "currentHeight": 0
        },
        "logHistory": []
    }

    # Write the user record to S3 using the username as the key
    object_key = f"users/{username}.json"
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=object_key,
        Body=json.dumps(body),
        ContentType='application/json'
    )

    # Return the API Gateway response
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({
            "message": "User created"
        })
    }
