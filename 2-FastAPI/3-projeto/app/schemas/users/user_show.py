from uuid import UUID
from pydantic import BaseModel, EmailStr

class UserDetail(BaseModel):
    user_id: UUID
    username: str
    email: EmailStr