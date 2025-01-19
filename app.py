from flask import request, make_response, redirect, render_template, session
from config.config import app

from models.LoginFormModel import LoginFormModel
from services.usuario_servicio import usuario

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", error=error)

@app.route("/")
def index():
    formLogin = LoginFormModel()

    return render_template('login.html', formLogin)

@app.route("/show")
def show():
    return render_template("show.html", **usuario)

@app.route("/cursos")
def cursos():
    return render_template("cursos.html", **usuario)

@app.route("/rutas")
def rutas():
    usuario_info = {
        'ip': session.get('user_ip'),
        'nombre': session.get('user_name')
    }
    return render_template('rutas.html', **usuario_info)
