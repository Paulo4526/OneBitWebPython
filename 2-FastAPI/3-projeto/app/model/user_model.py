# Beanie é um ODM (Object Document Mapper) que facilita a integração do MongoDB com Python
# Document: classe base usada para criar modelos de documentos que serão armazenados no MongoDB
# Indexed: usado para criar índices no banco, melhorando a performance de buscas em campos específicos
from beanie import Document, Indexed

# UUID é um identificador único universal (muito útil para identificar usuários, por exemplo)
# uuid4 é uma função que gera um UUID aleatório
from uuid import UUID, uuid4

# Field permite configurar os atributos (ex: valores padrão, validações) nos modelos do Pydantic
# EmailStr é um tipo especial do Pydantic que valida se uma string está no formato de e-mail
from pydantic import Field, EmailStr

# datetime representa uma data e hora (usado para obter quando o documento foi criado, por exemplo)
from datetime import datetime

# Optional permite que um campo aceite dois tipos: o tipo definido (ex: str) ou None (valor nulo)
from typing import Optional


#Criando nossa clase com o ODM beanie e atributos

# Define a classe User como um documento do banco, herdando de Document (do Beanie)
class User(Document):

    # Campo obrigatório: identificador único gerado automaticamente com uuid4
    user_id: UUID = Field(default=uuid4)

    # Campo de nome de usuário do tipo string
    # Indexed cria um índice no banco para esse campo, e unique=True garante que não pode haver duplicados
    username: Indexed(str, unique=True)

    # Campo de e-mail validado automaticamente pelo Pydantic como e-mail válido
    # Também é indexado e único (não podem existir dois usuários com o mesmo e-mail)
    email: Indexed(EmailStr, unique=True)

    # Campo obrigatório que representa a senha do usuário (geralmente uma hash da senha)
    has_password: str

    # Campo opcional para o primeiro nome do usuário (pode ser None)
    first_name: Optional[str] = None

    # Campo opcional para o sobrenome do usuário
    last_name: Optional[str] = None

    # Campo opcional para indicar se o usuário está desativado
    # (poderia ser booleano, mas aqui está como string — ex: "true" ou "false")
    disabled: Optional[str] = None

    # Metodo especial que define como o objeto é representado no modo debug
    # Exemplo: ao usar repr(user), mostrará algo como 'User email@example.com'
    def __repr__(self) -> str:
        return f'User {self.email}'
