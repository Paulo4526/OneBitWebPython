from pydantic import BaseModel, Field
from typing import Optional

class TaskCreate(BaseModel):
    title: str = Field(..., title='Título', min_length=3, max_length=50)
    description: str = Field(..., title='Descrição', min_length=3, max_length=150)
    status: Optional[bool] = False