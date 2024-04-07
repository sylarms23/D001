#importacion de APP
from flask_app import app

#importacion de CONTROLADORES
from flask_app.controllers import users_controllers
from flask_app.controllers import sucesos_controllers
from flask_app.controllers import likes_controllers


#ejecucion APP
if __name__=="__main__":
    app.run(debug=True) # aqui se podria cambiar el puerto asi: (debug = True, port=3400)


# pipenv install PyMySQL flask bcrypt

#pipenv install flask pymysql flask-bcrypt  (creo que esta funciona mejor para mi jaja)


#Para instalar de forma general en el pc:
#pip install Flask-Bcrypt
