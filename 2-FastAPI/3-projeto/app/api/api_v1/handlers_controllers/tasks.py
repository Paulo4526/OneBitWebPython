from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from app.schemas.tasks.task_cad import TaskCreate
from app.model.user_model import User
from app.model.task_model import Task
from app.schemas.tasks.task_show import TaskShow
from app.api.api_v1.dependencies.user_deps import get_current_user
from app.services.task_service import TaskService
from app.schemas.tasks.task_update import TaskUpdate
from typing import List
from uuid import UUID

task_router= APIRouter()

@task_router.get('/', summary='Lista as tarefas', response_model=List[Task])
async def list_tasks(user: User = Depends(get_current_user)):
    return await TaskService.list_taks(user)

@task_router.get('/{task_id}', summary='Detalhe de uma tarefa por id', response_model=Task)
async def task_detail(task_id: UUID, user: User = Depends(get_current_user)):
    task = await TaskService.task_detail(user, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada"
        )
    return task

@task_router.post('/create', summary='Adiciona Tarefa', response_model=Task)
async def create_task(data: TaskCreate, user: User = Depends(get_current_user)):
    return await TaskService.create_task(user, data)

@task_router.put('/{task_id}', summary='Atualiza task', response_model=Task)
async def task_update(task_id: UUID, data: TaskUpdate, user: User = Depends(get_current_user)):
    task = await TaskService.update_task(user, task_id, data)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada"
        )
    return task

@task_router.delete('/{task_id}', summary='Deleta a task')
async def task_delete(task_id: UUID, user: User = Depends(get_current_user)):
    success = await TaskService.delete_task(user, task_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada"
        )
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT,
        content={
            "message": "Tarefa deletada com sucesso",
            "task_id": str(task_id)
        }
    )