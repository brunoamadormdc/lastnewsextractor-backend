from flask import Blueprint,request,jsonify
import pytz
from classes.scrapper import Scrapper

scrapper = Scrapper()

scrap_routes = Blueprint('scrap_routes',__name__)
fuso_horario = pytz.timezone('America/Sao_Paulo')



@scrap_routes.route('/getlink',methods=['POST'])
def scraproutes():

        data = request.get_json()


        list = scrapper.scrapp(search=data['busca'],type=data['tipo'])

        return jsonify({
            'links':list,
            'count':len(list)
        }),200

@scrap_routes.route('/page',methods=['GET','POST'])
def scrapPages():

    if request.method == 'POST':
       data = request.get_json()
       print(data)
       list = scrapper.scrapPage(page=data['url'])

    return jsonify({
        'links':list,
        'count':len(list)
    }),200








