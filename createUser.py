import json
import boto3
import datetime

s3 = boto3.client('s3')

BUCKET_NAME = 'getfitdatabase-339713187152-us-east-2-an'

def lambda_handler(event, context):
    # Extract request info
    http_method = event.get('httpMethod') or event.get('requestContext', {}).get('http', {}).get('method', 'UNKNOWN')
    path = event.get('path') or event.get('rawPath', '/')
    request_body = json.parsevent.get('body') or '{}'

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

    # Write the request details to S3 with a timestamped key
    object_key = f"users/user1.json"
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
            "message": "Hello, World!",
            "saved_to": f"s3://{BUCKET_NAME}/{object_key}",
            "senderBody": request_body
        })
    }
