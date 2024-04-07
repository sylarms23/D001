#Importacion  FLASK
from flask import Flask

#inicializacion de APP
app = Flask(__name__)

#declaramos llave secreta se usa para la sesion
app.secret_key="1234"




