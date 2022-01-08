import re
import requests
from app import app
from werkzeug.utils import redirect
from models.imoveis import Imoveis
from flask import Blueprint, render_template, make_response, request


public_routes = Blueprint('imoveis_routes', __name__)

imoveis_models = Imoveis()


@public_routes.route('/index', methods=['GET'])
def index(): 
    imoveis = imoveis_models.imoveis()

    bairros = ['Ponta Negra', 'Petropolis', 'Tirol']

    return render_template('index.html', imoveis=imoveis , bairros=bairros)


@public_routes.route('/imovel/<id>',  methods=['GET'])
def imovel(id):
    print('teste')
    imovel = imoveis_models.imovel(imovel_id=id)

    if imovel is not None:
        return render_template('imovel.html', imovel=imovel)
    else:
        return redirect('/index')


@public_routes.route('/login', methods=['GET'])
def login():
    return render_template('login.html')
