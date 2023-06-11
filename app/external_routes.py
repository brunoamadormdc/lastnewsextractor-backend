from flask import Blueprint,request,jsonify
import pytz
from statics import tipos

external_routes = Blueprint('external_routes',__name__)
fuso_horario = pytz.timezone('America/Sao_Paulo')

@external_routes.route('/sites-list', methods=['GET'])
def sites_list():

    flatted_list = []

    for (key,value) in tipos.items():
        for item in value:
            flatted_list.append(item)
    
    return jsonify({
        'sites':flatted_list
    }),200

