#OBS: Sempre lembre de ativar o ambiente virtual desse projeto com o comando '.\.venv\Scripts\activate' no diretório principal
#Importando o Flask e o Render
from flask import Flask, render_template, request, redirect, url_for

#1 - Instanciando o flask
app = Flask(__name__)
titulo = "Python com Flask"
curso = [
    {"curso": "Manipulação de Dados", "nota": 5.6, "professor": "Giuliano de Andrade"},
    {"curso": "Herança e Templates", "nota": 6.3, "professor": "Paulo Bueno"},
    {"curso": "Integração de API", "nota": 6.8, "professor": "Margarida Ferreira"},
    {"curso": "Integração com Banco de dados", "nota": 7.0, "professor": "Paulo Martins"}
]

#Criando a rota localhost:5000/cursos
@app.route('/cursos', methods=["GET", "POST"])
def cursos():
    if request.method == "POST":
        # 1. Captura os dados do formulário
        nome = request.form.get("curso")
        nota = request.form.get("nota")
        professor = request.form.get("professor")

        # 2. Validação opcional (evitar valores nulos ou vazios)
        if nome and nota and professor:
            # 3. Converte nota para float e adiciona ao array
            novo_curso = {
                "curso": nome,
                "nota": float(nota),
                "professor": professor
            }
            curso.append(novo_curso)

            # Redireciona para GET (evita reenvio do POST)
            return redirect(url_for('cursos'))

    return render_template(
        "cursos.html",
        cursos = curso,
        titulo = titulo
    )
