#Importando o flask
from flask import Flask, render_template

#Instanciando o flask
app = Flask(__name__)
print(app)

#Criando rota localhost:5000/
@app.route('/')
def principal():
    return render_template("index.html") #Utilizando o render para renderizar as páginas view que por padrão no python se chama template
#Com o ambiente virtual ativo, digite o comando flask --app "diretório absoluto do arquivo que será rodado" run --debug
#Explicando o comando acima
#flask o comando principal
#--app o parametro para que possamos informar onde o nosso arquivo está por isso é seguido de um diretório absoluto do arquivo
#run para rodar o arquivo em flask
#--debug para que seja rodado em modo debug e não precisarmos sempre parar a aplicação a cada atualização

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")