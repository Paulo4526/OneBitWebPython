from fastapi import APIRouter
from app.api.api_v1.handlers_controllers import user_controller
from app.api.api_v1.auth.jwt import auth_router

router = APIRouter()

router.include_router(
    user_controller.user_router,
    prefix='/users',
    tags=['users']
)

router.include_router(
    auth_router,
    prefix='/auth',
    tags=['auth']
)