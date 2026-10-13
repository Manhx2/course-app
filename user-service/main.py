from fastapi import FastAPI

app = FastAPI(
    title="University Course - User Service",
    version="1.0.0"
)


@app.get("/health")
def health():
    return {
        "service": "user-service",
        "status": "healthy"
    }


@app.get("/users")
def get_users():
    return [
        {
            "id": 1,
            "username": "student01",
            "full_name": "Nguyen Van A",
            "role": "student"
        },
        {
            "id": 2,
            "username": "teacher01",
            "full_name": "Nguyen Van B",
            "role": "teacher"
        },
        {
            "id": 3,
            "username": "admin01",
            "full_name": "Administrator",
            "role": "admin"
        }
    ]

@app.get("/users/{user_id}")
def get_user(user_id: int):
    users = [
        {
            "id": 1,
            "username": "student01",
            "full_name": "Nguyen Van A",
            "role": "student"
        },
        {
            "id": 2,
            "username": "teacher01",
            "full_name": "Nguyen Van B",
            "role": "teacher"
        },
        {
            "id": 3,
            "username": "admin01",
            "full_name": "Administrator",
            "role": "admin"
        }
    ]

    for user in users:
        if user["id"] == user_id:
            return user

    from fastapi import HTTPException
    raise HTTPException(
        status_code=404,
        detail="User not found"
    )