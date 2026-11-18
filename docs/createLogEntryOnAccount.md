# Create Workout

## URL
POST /workout

## Description
Appends the given workout entry to the specified user's workout logs.

## Request Body Schema
```
{
    "username": str,
    "workout": {
        "equipment": str,
        "weight": float,
        "reps": float
    }
}
```

# Create Dietary Entry

## URL
POST /dietary

## Description
Appends the given dietary entry to the specified user's dietary logs.

## Request Body Schema
```
{
    "username": str,
    "dietaryEntry": {
        "name": str,
        "protein": float,
        "calories": int
    }
}
```

# Create Weight Entry

## URL
POST /weight

## Description
Appends the given weight entry to the specified user's weight logs.

## Request Body Schema
```
{
    "username": str,
    "weightEntry": {
        "weight": float
    }
}
```

# Create Height Entry

## URL
POST /height

## Description
Appends the given height entry to the specified user's height logs.

## Request Body Schema
```
{
    "username": str,
    "heightEntry": {
        "height": float
    }
}
```

