import json
import boto3

s3 = boto3.client('s3')

BUCKET_NAME = 'getfitdatabase-339713187152-us-east-2-an'

# Define expected structure of request body
schema = {
    "username": str,
    "index": int,
    "workout": {
            "equipment": str,
            "weight": float,
            "reps": int
        }
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

    # Get user's json from S3
    object_key = f"users/{request_body["username"]}.json"
    response = s3.get_object(Bucket=BUCKET_NAME, Key=object_key)
    data = json.loads(response['Body'].read())

    # Verify a workout exists at given index
    if request_body["index"] < 0 or request_body["index"] >= len(data["logHistory"]):
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "No workout exists at given index"})
        }

    # Edit workout at index in account
    index = request_body["index"]
    workout = data["logHistory"][index]
    workout["equipment"] = request_body["workout"]["equipment"]
    workout["weight"] = request_body["workout"]["weight"]
    workout["reps"] = request_body["workout"]["reps"]

    # store updated file back in S3
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=object_key,
        Body= json.dumps(data)
    )

    # Return 200
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(
            {
                "message": "Workout edited"
            }
        )
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