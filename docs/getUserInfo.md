# Get User

## URL
GET /account/`username`

## Description
Gets the specified user's file. This endpoint is different in that it does not have a request body, instead the username is in the URL.
So, to access the account with username "johndoe" you use `/account/johndoe`

## Response
```
{
    "plan": {
        "startDate": str,
        "goalWeight": int,
        "startWeight": int,
        "finishDate": str
    },
    "data": {
        "currentWeight": int,
        "currentHeight": int
    },
    "logHistory": [
        {
            "equipment": str,
            "weight": float,
            "reps": int,
            "timestamp": int
        }
    ]
}
```
