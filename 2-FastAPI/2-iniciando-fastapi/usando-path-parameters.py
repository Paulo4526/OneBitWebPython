#Lembresse de criar no 3-projeto um ambiente virtual com o comando: python -m venv .venv
#Ativando o ambiente virtual indo até o diretório venv criado, script e activate ex: .\.venv\Scripts/activated
#Instalar o fastapi com o comando: pip install fastapi
#Instalar o uvicorn com o comando: pip install uvicorn para iniciar o servidor
from fastapi import FastAPI

app = FastAPI()
#Dicionario de jogadores
jogadores = [
    {"id": 1, "nome":"Paulo Bueno", "idade":33, "data-nasc":"12-02-1991"},
    {"id": 2, "nome":"Carlos Bueno", "idade":45, "data-nasc":"12-02-1991"},
    {"id": 3, "nome":"Fabio Bueno", "idade":31, "data-nasc":"12-02-1991"},
    {"id": 4, "nome":"Roberio Bueno", "idade":37, "data-nasc":"12-02-1991"}
]
@app.get('/jogadores')
def lista_jogadores():
    return jogadores

#Buscando o jogador pelo ID pelo path parameter
#path(http://127.0.0.1:8000/busca-jogador/id_jogador)
@app.get('/busca-jogador/{jogador_id}')
def busca_jogador(jogador_id: int):
    for jogador in jogadores:
        if jogador['id'] == jogador_id:
            return jogador
    return {"erro": "Jogador não encontrado!"}

#Após definifir as rotas iniciar a aplicação com uvicorn comando: uvicorn (nome do arquivo):app --reload
#OBS: Garantir que o nome do arquivo não incie com numeros e que não tenha a extensão do arquivo, também é garantido que seja rodado o comando no mesmo diretório do arquivo
#Acessando documentação swagger com fastAPI: http://127.0.0.1:8000/docs
#Documentação com informações da api: http://127.0.0.1:8000/redoc