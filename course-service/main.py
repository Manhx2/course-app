from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI(
    title="University Course - Course Service",
    version="1.0.0"
)


@app.get("/health")
def health():
    return {
        "service": "course-service",
        "status": "healthy"
    }


@app.get("/courses")
def get_courses():
    return [
        {
            "id": 1,
            "code": "CS101",
            "name": "Introduction to Computer Science",
            "teacher": "teacher01"
        },
        {
            "id": 2,
            "code": "SE201",
            "name": "Software Engineering",
            "teacher": "teacher01"
        },
        {
            "id": 3,
            "code": "NET301",
            "name": "Computer Networks",
            "teacher": "teacher02"
        }
    ]

@app.get("/courses/{course_id}")
def get_course(course_id: int):
    courses = [
        {
            "id": 1,
            "code": "CS101",
            "name": "Introduction to Computer Science",
            "teacher": "teacher01"
        },
        {
            "id": 2,
            "code": "SE201",
            "name": "Software Engineering",
            "teacher": "teacher01"
        },
        {
            "id": 3,
            "code": "NET301",
            "name": "Computer Networks",
            "teacher": "teacher02"
        }
    ]

    for course in courses:
        if course["id"] == course_id:
            return course

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )