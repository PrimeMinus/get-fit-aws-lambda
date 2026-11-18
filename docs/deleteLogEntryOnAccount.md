# Delete Workout

## URL
DELETE /workout

## Description
Deletes the workout entry at the given index in the specified user's workout logs.

## Request Body Schema
```
{
    "username": str,
    "index": int
}
```

# Delete Dietary Entry

## URL
DELETE /dietary

## Description
Deletes the dietary entry at the given index in the specified user's dietary logs.

## Request Body Schema
```
{
    "username": str,
    "index": int
}
```

# Delete Weight Entry

## URL
DELETE /weight

## Description
Deletes the weight entry at the given index in the specified user's weight logs.

## Request Body Schema
```
{
    "username": str,
    "index": int
}
```

# Delete Height Entry

## URL
DELETE /height

## Description
Deletes the height entry at the given index in the specified user's height logs.

## Request Body Schema
```
{
    "username": str,
    "index": int
}
```

