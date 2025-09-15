from fastapi import APIRouter, HTTPException, status
from app.schemas.users.user_cad import UserAuth
from app.schemas.users.user_show import UserDetail
from app.services.user_service import UserService
from pymongo.errors import DuplicateKeyError

user_router = APIRouter()

@user_router.post('/adiciona', summary='Adiciona Usuário', response_model=UserDetail)
async def adiciona_usuario(data: UserAuth):
    try:
        return await UserService.create_user(data)
    except DuplicateKeyError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Usuário já existe')
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exc))