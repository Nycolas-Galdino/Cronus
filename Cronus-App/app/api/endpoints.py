from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_root():
    return {"message": "Bem-vindo ao Cronus API"}


@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    return {"task_id": task_id, "status": "pendente"}
