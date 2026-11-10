import json
import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')

BUCKET_NAME = 'getfitdatabase-339713187152-us-east-2-an'


def lambda_handler(event, context):

    # Get params from request URL
    username = event["pathParameters"]["username"]

    # Get user's json from S3
    object_key = f"users/{username}.json"

    # If user doesn't exist, return 404
    try:
        response = s3.get_object(Bucket=BUCKET_NAME, Key=object_key)
    except ClientError as e:
        error_code = e.response['Error']['Code']

        if error_code in ['404', 'NoSuchKey', 'NotFound']:
            return {
                "statusCode": 404,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps({
                    "message": "User not found"
                })
            }

        raise

    data = json.loads(response['Body'].read())

    # Return 200
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(data)
    }
