from fastapi import APIRouter

user_router = APIRouter()
@user_router.get('/test')
async def test():
    return f'Testtando o nosso projeto'