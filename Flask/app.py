from flask import Flask, render_template

app = Flask(__name__)  # flask utiliza a linguagem jinja2

### JEITO "na unha de" fazer, mas na prática é feito por templates
# @app.route("/", methods= ["get", "post"])  # "rotear" na raíz
# def index():
#     return "<html><form method = 'post' action='.'><input type= 'text' /><input type = 'submit' /></form></html>"

# @app.route("/pessoas")  # o que aparece para o usuário é esse nome e não o da
# #  função. Estará em http://127.0.0.1:5000/pessoas
# def pessoas():
#     return """\
#     <html>
#     <ul>
#         <li>fulano</li>
#         <li>ciclano</li>
#     </ul>
#     </html>
#     """

# app.run(debug=True)  # para rodar: python3.10 app.py para rodar
# #  sem refresh automático
# #  rodar com FLASK_ENV=development python3.10 app.py PARA refresh automático


@app.route("/", methods=["get", "post"])  # "rotear" na raíz
def index():
    return render_template("index.html", name="thiago")

@app.route("/pessoas")  # o que aparece para o usuário é esse nome e não o da
#  função. Estará em http://127.0.0.1:5000/pessoas
def pessoas():
    pessoas = [
        {"name": "ciclano"},
        {"name": "fulano"}
    ]
    return render_template("pessoas.html", pessoas=pessoas)

app.run(debug=True)  # para rodar: python3.10 app.py para rodar
#  sem refresh automático
#  rodar com FLASK_ENV=development python3.10 app.py PARA refresh automático
