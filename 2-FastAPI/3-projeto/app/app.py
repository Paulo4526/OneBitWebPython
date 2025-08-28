# Importa a classe principal do FastAPI usada para criar a aplicação web
from fastapi import FastAPI

# Importa o decorador para criar gerenciadores assíncronos de contexto (útil para startup/shutdown do app)
from contextlib import asynccontextmanager
import logging

# Importa as configurações da aplicação (ex: conexão com MongoDB, nome do projeto, prefixos de rota)
from app.core.config import settings

# Importa a função que inicializa o Beanie com os modelos e o banco MongoDB
from beanie import init_beanie

# Importa o cliente assíncrono oficial do MongoDB, usado para se conectar ao banco
from motor.motor_asyncio import AsyncIOMotorClient

# Importa o modelo de documento User, que será armazenado no MongoDB via Beanie
from app.model.user_model import User

from app.api.api_v1.router import router


# Define o gerenciador de ciclo de vida da aplicação (executado ao iniciar e encerrar a API)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Cria uma conexão com o banco MongoDB usando a string de conexão configurada, e acessa o banco 'todoapp'
    cliente_db = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).todoapp

    try:
        # Inicializa o Beanie com a conexão e a lista de modelos que representam os documentos do MongoDB
        await init_beanie(
            database=cliente_db,
            document_models=[
                # Lista de modelos (documentos) a serem registrados no banco
                User
            ]
        )
    except Exception as exc:
        logging.exception("Falha ao inicializar o Beanie/MongoDB. Continuando sem DB.")

    # Mantém a aplicação rodando durante o ciclo de vida
    yield

    # (Opcional) Aqui pode ser adicionado código para liberar recursos ou fechar conexões no shutdown
    # Ex: await cliente_db.close()

# Instancia o app FastAPI com título e rota da documentação definidos nas configurações,
# e define o gerenciador de ciclo de vida com o parâmetro lifespan
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f'{settings.API_V1_STR}/openapi.json',
    lifespan=lifespan
)

# OBS: Ao rodar o servidor (uvicorn main:app), você pode testar as rotas na interface Swagger:
# http://127.0.0.1:8000/docs

app.include_router(
    router,
    prefix=settings.API_V1_STR
)