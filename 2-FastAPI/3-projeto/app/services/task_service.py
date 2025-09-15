from app.model.user_model import User
from app.model.task_model import Task
from app.schemas.tasks.task_cad import TaskCreate
from app.schemas.tasks.task_update import TaskUpdate
from uuid import UUID

class TaskService:
    @staticmethod
    async def list_taks(user: User) -> list[Task]:
        #O owner.id e o user.id se refere ao id criado pelo benie não pela classe.
        tasks = await Task.find(Task.owner.id == user.id).to_list()
        return tasks

    @staticmethod
    async def create_task(user: User, data: TaskCreate) -> Task:
        task = Task(**data.dict(), owner=user)
        return await task.insert()

    @staticmethod
    async def task_detail(user: User, task_id: UUID) -> Task:
        # Use múltiplos filtros ao invés de operador & para compatibilidade
        task = await Task.find_one(
            Task.task_id == str(task_id),
            Task.owner.id == user.id
        )
        return task

    @staticmethod
    async def update_task(user: User, task_id: UUID, data: TaskUpdate) -> Task:
        task = await TaskService.task_detail(user, task_id)
        if not task:
            return None
        
        # Atualiza apenas os campos fornecidos
        update_data = data.dict(exclude_unset=True)
        if update_data:
            for field, value in update_data.items():
                setattr(task, field, value)
            await task.save()
        
        return task

    @staticmethod
    async def delete_task(user: User, task_id: UUID) -> bool:
        task = await TaskService.task_detail(user, task_id)
        if task:
            await task.delete()
            return True
        return False
