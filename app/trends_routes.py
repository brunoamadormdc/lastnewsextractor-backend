from flask import Blueprint,request,jsonify
import pytz
from classes.googletrends import GoogleTrends

trends_routes = Blueprint('trends_routes',__name__)
fuso_horario = pytz.timezone('America/Sao_Paulo')

@trends_routes.route('/get-trends/<country>', methods=['GET'])
def trendsroutes(country):

        trends = GoogleTrends(country=country)
        trends.get_trends_brazil()
        words = trends._words

        return jsonify({
            'trends':words,
        }),200