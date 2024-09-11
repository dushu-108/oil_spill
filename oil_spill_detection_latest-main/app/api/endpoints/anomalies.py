from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_anomalies():
    return {"message": "This is a placeholder for anomalies data"}
