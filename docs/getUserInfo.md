# Get User

## URL
GET /account/`username`

## Description
Gets the specified user's file. This endpoint is different in that it does not have a request body, instead the username is in the URL.
So, to access the account with username "johndoe" you use `/account/johndoe`

## Expected Response Structure
```
{
    "plan": {
        "startDate": str,
        "goalWeight": float,
        "startWeight": float,
        "finishDate": str
    },
    "data": {
        "currentWeight": float,
        "currentHeight": float
    },
    "logs": {
        "workout": [
            {
                "equipment": str,
                "weight": float,
                "reps": int,
                "timestamp": int
            }
        ],
        "dietary": [
            {
                "name": str,
                "protein": float,
                "calories": int,
                "timestamp": int
            }
        ],
        "weight": [
            {
                "weight": float
                "timestamp": int
            }
        ],
        "height": [
            {
                "height": float,
                "timestamp": int
            }
        ]
    }
}
```
