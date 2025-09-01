from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from app.model.user_model import User
from jose import jwt
from app.core.config import settings

oauth_reusable = OAuth2PasswordBearer(
    tokenUrl=f'{settings.API_V1_STR}/auth/login',
    scheme_name='JWT'
)

async def get_current_user(token: str =Depends(oauth_reusable)) -> User:
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            settings.ALGORITHM
        )
        #token data
        
    except:
        pass