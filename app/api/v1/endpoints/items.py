from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def get_items():
    return [{"id": 1, "name": "tool"}, {"id": 2, "name": "key"}, {"id": 3, "name": "bread"}]
