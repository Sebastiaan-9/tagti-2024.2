#python -m venv venv
#.\venv\Scripts\activate
#pip install flask
# pip install python-dotenv
#pip freeze > requirements.txt
#pip install -r requirements.txt
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/cardapio')
def cardapio():
    pizzas = [
        {
            "nome": "Calabresa",
            "ingredientes": "Molho de tomate, mussarela, calabresa, cebola e orégano",
            "preco": 30.00
        },
        {
            "nome": "Mussarela",
            "ingredientes": "Molho de tomate, mussarela e orégano",
            "preco": 25.00
        },
        {
            "nome": "Portuguesa",
            "ingredientes": "Molho de tomate, mussarela, presunto, ovos, cebola, azeitona e orégano",
            "preco": 35.00
        }
    ]
    return render_template("cardapio.html", pizzas=pizzas)

@app.route('/avaliacoes')
def avaliacoes():
    avaliacoes = [
        {
            "nome": "Charlie",
            "pizza": "Calabresa",
            "avaliacao": "3 estrelas",
            "comentario": "Achei a pizza muito salgada!",
            "data": "25/11/2024"
        },
        {
            "nome": "Adam",
            "pizza": "Mussarela",
            "avaliacao": "4 estrelas",
            "comentario": "Achei a pizza muito boa! Comprarei mais com certeza.",
            "data": "25/11/2024"
        }
    ]
    return render_template('avaliacoes.html', avaliacoes=avaliacoes)

@app.route('/contatos')
def contatos():
    contatos = [
        {
            "email": "brenoprof1@gmai.co",
            "telefone": "87 993094892"
        }
    ]
    return render_template('contatos.html', contatos=contatos)

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
