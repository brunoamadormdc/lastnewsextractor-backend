import flask
from flask_cors import CORS
from app.scrap_routes import scrap_routes

app = flask.Flask(__name__)
cors = CORS(app, origins='*')

app.register_blueprint(scrap_routes, url_prefix='/scrap')
