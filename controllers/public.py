import requests
from app import app
from werkzeug.utils import redirect
from flask import Blueprint, render_template, make_response, request


public_routes = Blueprint('imoveis_routes', __name__)


@public_routes.route('/index', methods=['GET'])
def login():

    return render_template('index.html')

@public_routes.route('/index', methods=['POST'])
def login_form():
    email = request.form.get('email')
    senha = request.form.get('senha')

    req = requests.post(url='http://127.0.0.1:5000/api/usuarios/login', data={'email': email, 'senha':senha})
    json = req.json()
    info = req.headers
    cookie = info['Set-Cookie']
    
    print(cookie)

    if json['codigo-requisicao'] == 'in200':
        resp = make_response(render_template('logado.html'))
        resp.set_cookie('session', cookie)
        return resp
       
    else:
        return render_template('erro404.html')


@public_routes.route('/logado', methods=['GET'])
def logado():
    cookie = request.cookies.get('session')
    req = requests.get('http://127.0.0.1:5000/api/imoveis/meus_imoveis', headers={'Cookie': cookie})

    json = req.json()
    print(json)
    if json['codigo-requisicao'] == 'in300':
        return redirect('/index')
    else:
        return render_template('logado.html')


