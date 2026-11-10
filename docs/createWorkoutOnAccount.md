# Create Workout

## URL
POST /workout

## Description
Adds the given workout to the specified user's account.

## Request Body
```
{
	"username": str,
	"workout": 
			{
				"equipment": str,
				"weight": float,
				"reps": int
			}
}
```
