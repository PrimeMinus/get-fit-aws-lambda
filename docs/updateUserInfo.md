# Update Account Details

## URL
PATCH /account

## Description
Edits the details on the specified user's account.
Does not modify workouts.

## Request Body
```
{
    "username": str,
    "newData": {
        "plan": {
            "startDate": str,
            "goalWeight": int,
            "startWeight": int,
            "finishDate": str
        },
        "data": {
            "currentWeight": int,
            "currentHeight": int
        }
    }
}
```
