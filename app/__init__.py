import flask
from flask_cors import CORS
from app.scrap_routes import scrap_routes
from app.trends_routes import trends_routes
from app.external_routes import external_routes

app = flask.Flask(__name__)

cors = CORS(app, origins='*')

app.register_blueprint(scrap_routes, url_prefix='/scrap')
app.register_blueprint(trends_routes, url_prefix='/trends')
app.register_blueprint(external_routes, url_prefix='/external')
