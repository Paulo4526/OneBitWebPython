#Lembresse antes de iniciar a instalação do FastAPI, criar um novo ambiente virtual com os comandos:
# - python -m venv .venv -> Para criar um novo ambiente chamado de .venv
# - .\.venv\Scripts\activate -> Para ativar o ambiente virtual.
#- Instalando o pydantic com o comando: pip install pydant
from pydantic import BaseModel
from pydantic.v1 import validator

#Sem pydantic
user = {
    "nome": "Paulo Bueno",
    "idade": 25,
    "email": "paulobueno@outlook.com"
}
print(user)

class User(BaseModel):
    name: str
    idade: int
    email: str

    @validator('email')
    def validate_email(cls, value):
        if '@' not in value:
            raise ValueError('E-mail está inválido!')
        return value

#Com pydantic, uma tipagem parecida com Java, instanciando um construtor já com um valor
user1 = User(
    name= "Paulo",
    idade = 33,
    email = "paulosilvabueno@hotmail.com"
)
