# Delete Workout

## URL
DELETE /workout

## Description
Deletes the workout at the given index on the specified user's account.

## Request Body
```
{
	"username": str,
	"index": int
}
```
> [!NOTE]
> `index` is the index of the entry in `logHistory` that you wish to update.
