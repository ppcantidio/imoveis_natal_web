import re
import requests
from app import app
from werkzeug.utils import redirect
from flask import Blueprint, render_template, make_response, request


public_routes = Blueprint('imoveis_routes', __name__)

def api(endpoint):
    return f'http://127.0.0.1:5000/api/{endpoint}'


@public_routes.route('/index', methods=['GET'])
def index(): 
    response = requests.get(url=api('/imoveis/busca'), params={'categoria': 'venda'})
    response = response.json()

    imoveis = response['imoveis']

    bairros = ['Ponta Negra', 'Petropolis', 'Tirol']

    cont = 0
    for imovel in imoveis:
        corretor_id = imovel['corretor_id']
        response_corretor = requests.get(url=api(f'usuarios/info/{corretor_id}'))
        response_corretor = response_corretor.json()

        corretor = response_corretor['corretor']
        imovel['corretor_nome'] = corretor['nome']

        valor = '{0:,}'.format(imoveis[cont]['valor'])
        imoveis[cont]['valor'] = valor.replace(',', '.')

        imoveis[cont]['bairro'] = imoveis[cont]['bairro'].title()

        cont += 1

    return render_template('index.html', imoveis=imoveis , bairros=bairros)



@public_routes.route('/imovel', methods=['GET'])
def imovel():
    return render_template('imovel.html')




@public_routes.route('/imovel/<id>', methods=['GET'])
def imovel_page(id):
    response = requests.get(url=api('imovel'), params={'imovel_id': id})
    response_json = response.json()
    response_code =  response.status_code

    if response_json['codigo-requisicao'] != 'in200':
        return render_template('imovel.html', imoveis=[] , bairros=[])

    imovel = response_json['imovel']

    return render_template('imovel.html', imovel)


# @public_routes.route('/imovel/busca', methods='GET')
# def busca_personalizada():
#     tipo = request.args.get('tipo')
#     categoria = request.args.get('categoria')
#     bairro = request.args.get('bairro')
#     valor = request.args.get('valor')
#     quartos = request.args.get('quartos')
#     imovel_id = request.args.get('imovel_id')
#     corretor_id = request.args.get('corretor_id')

#     params = {}
#     if tipo is not None:
#         params['tipo'] = tipo

#     if categoria is not None:
#         params['categoria'] = categoria

#     if bairro is not None:
#         params['bairro'] = bairro

#     if valor is not None:
#         params['valor'] = valor

#     if quartos is not None:
#         params['quartos'] = quartos

#     if imovel_id is not None:
#         params['imovel_id'] = imovel_id

#     if corretor_id is not None:
#         params['corretor_id'] = corretor_id

#     response = requests.get(url=api('imoveis/busca'), params=params)
#     response_json =  response.json()

#     if response_json['codigo-requisicao'] == 'in200':
#         return render_template('index.html', imoveis=response_json['imoveis'])

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


# @public_routes.route('/uploadteste', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'GET':
#         return """
#         <form method="POST" enctype="multipart/form-data" action="POST">
#             <input type="file" name="file[]" multiple="">
#             <input type="submit" value="add">
#         </form>
#         """

#     else:
#         uploaded_files = request.files.getlist("file[]")
#         print (uploaded_files)
#         return ""