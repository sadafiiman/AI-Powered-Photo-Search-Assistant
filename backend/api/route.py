from fastapi import APIRouter
from services.job_service import create_job, get_job
from schemas.job import JobCreateResponse, JobStatusResponse

router = APIRouter()


@router.post("/upload", response_model=JobCreateResponse)
def upload_image():
    job = create_job()
    return JobCreateResponse(id=str(job.id), status=job.status)


@router.get("/job/{job_id}", response_model=JobStatusResponse)
def job_status(job_id: str):
    job = get_job(job_id)

    return JobStatusResponse(
        id=str(job.id),
        status=job.status,
        extracted_keywords=job.extracted_keywords,
        results=job.results
    )