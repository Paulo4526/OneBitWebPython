from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password):
    return password_context.hash(password)

#Criptografia da Senha
def get_password_hash(password: str) -> str:
    return password_context.hash(password)

#Descriptografar a Senha
def verify_password(password: str, hashed_password: str) -> bool:
    return password_context.verify(password, hashed_password)