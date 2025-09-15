from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from app.model.user_model import User
from jose import jwt, JWTError
from app.core.config import settings
from app.schemas.auth.auth_schema import TokenPayload
from datetime import datetime
from pydantic import ValidationError
from app.services.user_service import UserService

oauth_reusable = OAuth2PasswordBearer(
    tokenUrl=f'{settings.API_V1_STR}/auth/login',
    scheme_name='JWT'
)

async def get_current_user(token: str = Depends(oauth_reusable)) -> User:
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        token_data= TokenPayload(**payload)
        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Token foi expirado',
                headers={'WWW-Authenticate': 'Bearer'}
            )
    except(JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Erro na validação do token',
            headers={'WWW-Authenticate': 'Bearer'}
        )

    user = await UserService.get_user_by_id(token_data.sub)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Não foi possível encontrar o usuário',
            headers={'WWW-Authenticate': 'Bearer'}
        )
    return user