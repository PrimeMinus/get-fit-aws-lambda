# Edit Workout Entry

## URL
PATCH /workout

## Description
Edits the workout entry at the given index in the specified user's workout logs.

## Request Body Schema
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

# Edit Dietary Entry

## URL
PATCH /dietary

## Description
Edits the dietary entry at the given index in the specified user's dietary logs.

## Request Body Schema
```
{
    "username": str,
    "index": int,
    "dietaryEntry": {
        "name": str,
        "protein": float,
        "calories": int
    }
}
```

# Edit Weight Entry

## URL
PATCH /weight

## Description
Edits the weight entry at the given index in the specified user's weight logs.

## Request Body Schema
```
{
    "username": str,
    "index": int,
    "weightEntry": {
        "weight": float
    }
}
```

# Edit Height Entry

## URL
PATCH /height

## Description
Edits the height entry at the given index in the specified user's height logs.

## Request Body Schema
```
{
    "username": str,
    "index": int,
    "heightEntry": {
        "height": float
    }
}
```

