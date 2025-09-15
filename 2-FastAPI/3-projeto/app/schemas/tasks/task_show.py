from pydantic import BaseModel, Field
from datetime import datetime

class TaskShow(BaseModel):
    task_id: str
    status: bool
    title: str
    description: str
    created_at: datetime
    updated_at: datetime
