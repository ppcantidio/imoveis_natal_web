from app import app
from flask import request, jsonify, Blueprint, render_template
from bson.objectid import ObjectId


home_routes = Blueprint('home_routes', __name__)


@home_routes.route('/', methods=['GET'])
def home():
    return 'Seja bem vindo a API de integracão do IMOVEIS NATAL'


@home_routes.after_request # blueprint can also be app~~
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response


@app.errorhandler(404)
def page_not_found(e):
    return render_template('erro404.html')


@app.errorhandler(500)
def erro_api(e):
    return render_template('erro500.html')