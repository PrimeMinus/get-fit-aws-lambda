# Edit Workout

## URL
PATCH /workout

## Description
Edits the workout at the given index on the specified user's account.

## Request Body
```
{
  "username": str,
  "index": int,
  "workout": {
        "equipment": str,
        "weight": float,
        "reps": int
      }
}
```
> [!NOTE]
> `index` is the index of the entry in `logHistory` that you wish to update.
