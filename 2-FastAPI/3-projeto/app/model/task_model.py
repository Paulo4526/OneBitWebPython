from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, Indexed, Link, before_event, Replace, Insert
from pydantic import Field
from app.model.user_model import User

class Task(Document):
    task_id: Indexed(str, unique=True) = Field(default_factory=lambda: str(uuid4()))
    status: bool = False
    title: str
    description: str
    owner: Link[User]
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    def __repr__(self) -> str:
        return f'Task {self.title}'

    def __str__(self) -> str:
        return self.title

    def __hash__(self) -> str:
        return hash(self.title)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Task):
            return self.task_id == other.task_id
        return False

    @before_event([Replace, Insert])
    def sync_update_at(self):
        self.updated_at = datetime.now()