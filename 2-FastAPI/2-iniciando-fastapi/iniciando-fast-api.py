#Lembresse de criar no 3-projeto um ambiente virtual com o comando: python -m venv .venv
#Ativando o ambiente virtual indo até o diretório venv criado, script e activate ex: .\.venv\Scripts/activated
#Instalar o fastapi com o comando: pip install fastapi
#Instalar o uvicorn com o comando: pip install uvicorn
from fastapi import FastAPI

#Instanciando o FastAPI
app = FastAPI()

#Criando rotas
@app.get('/')
def inicio():
    return {"Menssagem": "Olá mundo!"}
#Após definifir as rotas iniciar a aplicação com uvicorn comando: uvicorn (nome do arquivo):app --reload
#OBS: Garantir que o nome do arquivo não incie com numeros e que não tenha a extensão do arquivo, também é garantido que seja rodado o comando no mesmo diretório do arquivo
#Acessando documentação swagger com fastAPI: http://127.0.0.1:8000/docs
#Documentação com informações da api: http://127.0.0.1:8000/redoc