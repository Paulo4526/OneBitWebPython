#Lembresse antes de iniciar a instalação do FastAPI, criar um novo ambiente virtual com os comandos:
# - python -m venv .venv -> Para criar um novo ambiente chamado de .venv
# - .\.venv\Scripts\activate -> Para ativar o ambiente virtual.
# - Instalar o mypy para verificação da correta tipagem comando: "pip install mypy"
# - Para verificar se a escrita do código está conforme a tipagem correta: mypy "nome ou diretório absoluto com o arquivo python"

#Sem type hint
def hello(name):
    return f'Olá {name}, seja bem vindo ao curso de FastAPI!'

#Com Type Hint, tipagem em python
def hello2(name: str) -> str:
    return f'Olá {name}, seja bem vindo ao curso de FastAPI!'

#Lista sem Type Hint
hintlist = [
    "Paulo Bueno", "Antonia Barros"
]

#Lista com Type Hint
hintlist2: list[str] = [
    "Paulo", "Antonia"

]

#Dicionario sem Type Hint
hint_dict = {
    10: "Paulo Bueno",
    11: "Carlos Bueno"
}

#Dicionario com Type Hint
hint_dict2: dict[int, str | list[dict[int, str]]] = {
    1: "Paulo Bueno",
    2: [
        {20: "Paulo"},
        {30: "Bueno"}
    ]
}
print(hello2("Paulo Bueno"))
