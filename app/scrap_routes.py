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

@scrap_routes.route('/scrap-unique',methods=['POST'])
def scrap_unique():

        data = request.get_json()

        list = scrapper.scrapp_unique(search=data['busca'],pages=data['page'])

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

@scrap_routes.route('/get_resume', methods=['POST'])
def scrap_resume():
    
    data = request.get_json()
    youtube = False
    prompt = data['prompt']
    page = data['url']

    if page.find('youtube.com') != -1:
        youtube = True


    if youtube:
        resume = scrapper.scrap_get_resume_youtube(url=page,prompt=prompt)
    else:
        resume = scrapper.scrap_get_resume(url=page,prompt=prompt)
    
    return jsonify({
        'resume':resume
    }),200









