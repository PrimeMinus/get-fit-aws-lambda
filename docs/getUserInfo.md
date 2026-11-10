# Get User

## URL
GET /account

## Description
Gets the specified user's file

## Request Body
```
{
    "username": str
}
```

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
