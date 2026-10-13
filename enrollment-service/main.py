
from fastapi import FastAPI, HTTPException
import httpx
import os

app = FastAPI(
    title="University Course - Enrollment Service",
    version="1.0.0"
)

USER_SERVICE_URL = os.getenv(
    "USER_SERVICE_URL",
    "http://127.0.0.1:8001"
)

COURSE_SERVICE_URL = os.getenv(
    "COURSE_SERVICE_URL",
    "http://127.0.0.1:8002"
)

ENROLLMENTS = [
    {
        "id": 1,
        "student_id": 1,
        "course_id": 1,
        "status": "enrolled"
    },
    {
        "id": 2,
        "student_id": 1,
        "course_id": 2,
        "status": "enrolled"
    },
    {
        "id": 3,
        "student_id": 2,
        "course_id": 3,
        "status": "enrolled"
    }
]


@app.get("/health")
def health():
    return {
        "service": "enrollment-service",
        "status": "healthy"
    }


@app.get("/enrollments")
def get_enrollments():
    return ENROLLMENTS


@app.get("/enrollments/{enrollment_id}/details")
async def get_enrollment_details(enrollment_id: int):
    enrollment = next(
        (item for item in ENROLLMENTS
         if item["id"] == enrollment_id),
        None
    )

    if enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            user_response = await client.get(
                f"{USER_SERVICE_URL}/users/"
                f"{enrollment['student_id']}"
            )
            user_response.raise_for_status()

            course_response = await client.get(
                f"{COURSE_SERVICE_URL}/courses/"
                f"{enrollment['course_id']}"
            )
            course_response.raise_for_status()

        return {
            "enrollment_id": enrollment["id"],
            "status": enrollment["status"],
            "student": user_response.json(),
            "course": course_response.json()
        }

    except httpx.HTTPStatusError as exc:
        raise HTTPException(
            status_code=502,
            detail="A dependent service returned an error"
        ) from exc

    except httpx.RequestError as exc:
        raise HTTPException(
            status_code=503,
            detail="A dependent service is unavailable"
        ) from exc
