import json
import boto3
import datetime

BUCKET_NAME = 'getfitdatabase-339713187152-us-east-2-an'  # Replace with your S3 bucket name
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Same object within create user, get objet from the same bucket, and loading the information stored
    object_key = f"users/user1.json"
    response = s3.get_object(Bucket=BUCKET_NAME, Key=object_key)
    body = json.loads(response['Body'].read().decode('utf-8'))
    # Return response to the gateway
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(body)
}