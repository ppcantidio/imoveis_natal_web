from flask import Flask

app = Flask(__name__, static_folder='templates/static')

from controllers.public import public_routes
from controllers.home import home_routes

app.register_blueprint(home_routes)
app.register_blueprint(public_routes)