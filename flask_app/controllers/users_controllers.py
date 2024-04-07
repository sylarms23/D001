#importaciones
from flask import Flask, render_template, request, redirect, session, flash

#importar la app
from flask_app import app

#importar todos los modelos
from flask_app.models.usuarios import Usuario
from flask_app.models.sucesos import Suceso
from flask_app.models.likes import Like

#importamos BCrypt
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#Rutas
@app.route('/')
def index():
    return render_template('login_registro.html')


@app.route("/registrar", methods=["POST"])
def registrar():
    #request.form ={"nombre": "Elena", "apellido": "De Troya"........}

    #validar que la info sea correcta
    if not Usuario.validar_usuario(request.form):
        #no es valida la info,redireccionamos al formulario
        return redirect("/")
    
    #encriptamos la contraseña
    pass_encrypt = bcrypt.generate_password_hash(request.form["password"])
    #genera un diccionario con toda la info y solo la CONTRASEÑA encriptada
    form = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "correo": request.form['correo'],
        "password": pass_encrypt # AQUI SE GUARDA LA CONTRASEÑA ENCRIPTADA
    }

    nuevo_id = Usuario.guardar(form) #recibiendo el ID del nuevo Ususario
    session['usuario_id'] = nuevo_id
    return redirect("/dashboard")
    
@app.route("/dashboard")
def dashboard():
    #verificar que el usuario inicio sesion(hay una sesion cuando se regitra y tambien cuando hace login)
    if 'usuario_id' not in session:
        return redirect("/")
    
    #crear una instancia del usuario en base a la sesion(para poder entregar datos del usuario al html dashboard)
    form = {"id": session['usuario_id']}
    usuario = Usuario.obtener_por_id(form)

    sucesos = Suceso.obtener_todos()

    cant_si = Like.cant_si()
    cant_no = Like.cant_no()

    return render_template("dashboard.html", usuario=usuario, sucesos=sucesos, cant_si=cant_si, cant_no=cant_no)


@app.route("/login", methods=["POST"])
def login():
    #request.form ={"correo": "elena@gd.com", "password": "Hola123"........}
    #verificamos que el correo no exista en la BD
    usuario = Usuario.obtener_por_correo(request.form) #usuario = instancia Usuario ó False

    print(usuario)

    if not usuario:
        flash("E-mail no registrado", "login")
        print("se deberia ejecutar el flash")
        return redirect("/")
    #si usuario SI es instancia de Usuario
    if not bcrypt.check_password_hash(usuario.password, request.form["password"]): #contraseña encriptada v/s contraseña no encriptada
        flash("Password incorrrecto", "login")
        return redirect("/")
    
    session['usuario_id'] = usuario.id #guardado en sesion el ID del usuario
    return redirect("/dashboard")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/test")
def test():
    
    cant_si = Like.cant_si()
    suceso_id = 5

    cant_no = Like.cant_no()

    return render_template("test.html",cant_si=cant_si, suceso_id=suceso_id, cant_no=cant_no)


