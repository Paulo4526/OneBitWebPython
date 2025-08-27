from app.model.user_model import User
from app.schemas.user_cad import UserAuth
from app.core.secutiry import get_password_hash

class UserService:
    @staticmethod
    async def create_user(user: UserAuth):
        usuario = User(
            username = user.username,
            email = user.email,
            has_password=get_password_hash(user.password)
        )
        await usuario.save()
        return usuario