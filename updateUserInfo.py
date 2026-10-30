import json
import boto3
import datetime

s3 = boto3.client('s3')

BUCKET_NAME = 'getfitdatabase-339713187152-us-east-2-an'  # Replace with your S3 bucket name

def lambda_handler(event, context):
    object_key = f"users/user1.json"
    response = s3.get_object(Bucket=BUCKET_NAME, Key=object_key)
    data = json.loads(response['Body'].read())
    data['user'] ='updated_val'
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key='data.json',
        Body=json.dumps(data)
    )
    # 
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(body)
    }
