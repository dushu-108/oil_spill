from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_satellite_data():
    return {"message": "This is a placeholder for satellite data"}
