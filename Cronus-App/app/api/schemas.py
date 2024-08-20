from pydantic import BaseModel
from datetime import datetime


class TaskSchema(BaseModel):
    id: int
    name: str
    due_date: datetime
    is_completed: bool = False

    class Config:
        orm_mode = True
