#Lembresse de criar o arquivo .env e colocar as variaveis de ambiente lá no diretório app do python
# Importa o tipo List da biblioteca typing para tipar listas (usado para CORS)
from typing import List

# Importa a função config da biblioteca python-decouple para acessar variáveis do .env
from decouple import config

# Importa o tipo AnyHttpUrl do Pydantic, que valida URLs para uso em CORS
from pydantic import AnyHttpUrl

# Importa a classe base BaseSettings do Pydantic Settings, usada para configuração baseada em ambiente
from pydantic_settings import BaseSettings


# Cria a classe Settings que herda de BaseSettings (suporta carregamento automático via .env)
class Settings(BaseSettings):

    # Prefixo padrão das rotas da API (ex: /api/v1/usuarios)
    API_V1_STR: str = '/api/v1'

    # Chave secreta usada para gerar o token de acesso JWT, vinda do .env
    JWT_SECRET_KEY: str = config('JWT_SECRET_KEY', cast=str, default='changeme')

    # Chave secreta usada para gerar o token de refresh JWT, também lida do .env
    JWT_REFRESH_SECRET_KEY: str = config('JWT_REFRESH_SECRET_KEY', cast=str, default='changeme')

    # Algoritmo usado para assinar os tokens JWT (padrão: HS256)
    ALGORITHM: str = 'HS256'

    # Tempo de expiração do token de acesso (em minutos) — aqui: 60 minutos
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Tempo de expiração do token de refresh — aqui: 7 dias (60 min × 24 h × 7)
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    # Lista de URLs permitidas para fazer requisições à API (CORS); inicialmente vazia
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    # Nome do projeto (usado, por exemplo, no título da documentação Swagger)
    PROJECT_NAME: str = "TODOFast"

    # String de conexão com o MongoDB, também lida do .env
    MONGO_CONNECTION_STRING: str = config("MONGO_CONNECTION_STRING", cast=str, default='mongodb://localhost:27017')

    # Subclasse interna para configurar o comportamento da classe Settings
    class Config:
        # Define que os nomes das variáveis devem ser sensíveis a maiúsculas/minúsculas
        case_sensitive = True


#Instanciando a classe Settings()
settings = Settings()