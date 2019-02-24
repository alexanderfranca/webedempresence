
from flask import Flask, render_template, redirect, url_for, session, request
import re
from webpresence.link import Link
from webpresence.presence import Presence

app = Flask(__name__)

@app.route('/')
def home():

    return render_template("home.html")


@app.route('/get_link', methods=['GET', 'POST'])
def get_link():

    matricula = request.form.get('matricula')
    cpf = request.form.get('cpf')

    link = Link(host='localhost', user='edempresence', password='3d3mzeppelin%ZEPPELIN', database='edempresence', webhost='http://edem.ddns.net:5000/show_presences')

    cpf_ok = link.check_cpf(matricula=matricula, cpf=cpf)

    if cpf_ok:
        user_link = link.get_link(matricula=matricula)
        return render_template('show_link.html', link=user_link).encode('utf8')
    else:
        return render_template('home.html', message='Dados nao encontrados. Verifique o numero de matricula e CPF do responsavel.')

@app.route('/show_presences', methods=['GET'])
def show_presences():

    matricula = request.args.get('matricula')
    cpf = request.args.get('cpf')

    presence = Presence(host='localhost', user='edempresence', password='3d3mzeppelin%ZEPPELIN', database='edempresence')

    presences = presence.get_presence(matricula=matricula)

    return render_template('presences.html', presences=presences)
    

if __name__ == "__main__":
    app.run(host='0.0.0.0')

