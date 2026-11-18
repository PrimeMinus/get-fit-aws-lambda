# Update Account Details

## URL
PATCH /account

## Description
Edits the details on the specified user's account.
Does not modify logs.

## Request Body
```
{
    "username": str,
    "newData": {
        "plan": {
            "startDate": int,
            "goalWeight": float,
            "startWeight": float,
            "finishDate": int
        },
        "data": {
            "currentWeight": float,
            "currentHeight": float
        }
    }
}
```
