import json
import boto3
import datetime

s3 = boto3.client('s3')

BUCKET_NAME = 'getfitdatabase-339713187152-us-east-2-an'

# Define expected structure of request body
schema = {
    "username": str
}

def lambda_handler(event, context):

    # Parse request body
    raw_body = event.get('body') or '{}'
    try:
        request_body = json.loads(raw_body) if isinstance(raw_body, str) else raw_body
    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "Request body must be valid JSON"})
        }

    # Verify that request body matches schema
    if not matches_structure(request_body, schema):
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "Request body JSON must conform to schema"})
        }

    # Validate username
    # TODO: Add validation that username conforms to some standard (no spaces and such)
    username = request_body["username"]
    if username == "":
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "username cannot be empty"})
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

# Helper function to check if json matches schema
def matches_structure(data, schema):
    if isinstance(schema, dict):
        return (
            isinstance(data, dict)
            and data.keys() == schema.keys()
            and all(
                matches_structure(data[key], value)
                for key, value in schema.items()
            )
        )

    return type(data) == schema