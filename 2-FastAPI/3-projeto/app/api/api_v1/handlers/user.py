from fastapi import APIRouter, HTTPException, status
from app.schemas.user_cad import UserAuth
from app.schemas.user_show import UserDetail
from app.services.user_service import UserService
import pymongo

user_router = APIRouter()
@user_router.get('/test')
async def test():
    return f'Testtando o nosso projeto'

@user_router.post('/adiciona', summary='Adiciona Usuário', response_model=UserDetail)
async def adiciona_usuario(data: UserAuth):
    try:
        return await UserService.create_user(data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))