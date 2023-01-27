from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/energy")


@router.get("/")
async def get_all_managers():
    return {"Elements": []}
