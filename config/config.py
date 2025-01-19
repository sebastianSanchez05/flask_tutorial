from flask import Flask
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'CLAVE_SEGURA'
bootstrap = Bootstrap(app)