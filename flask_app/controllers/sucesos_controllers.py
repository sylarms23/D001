#importaciones
from flask import Flask, render_template, request, redirect, session, flash

#importar la app
from flask_app import app

#importar todos los modelos
from flask_app.models.sucesos import Suceso
from flask_app.models.usuarios import Usuario
from flask_app.models.likes import Like

#importamos BCrypt
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


#Rutas
@app.route('/nuevo/suceso')
def nuevo_suceso():
    #verificar que el usuario inicio sesion
    if 'usuario_id' not in session:
        return redirect("/")
    
    form = {"id": session['usuario_id']}
    usuario = Usuario.obtener_por_id(form)
    
    return render_template("nuevo_suceso.html", usuario=usuario)


@app.route('/crear', methods=["POST"])
def crear_suceso():
    #verificar que el usuario inicio sesion
    if 'usuario_id' not in session:
        return redirect("/") #envia a login
    
    #validar que la info del suceso es correcta
    if not Suceso.validar_suceso(request.form):
        return redirect("/nuevo/suceso")
    
    #guardar el suceso
    Suceso.guardar(request.form)
    #redireccionar al dashborad
    return redirect("/dashboard")
    

@app.route('/editar/suceso/<int:id>')
def editar_suceso(id):
    #verificar que el usuario inicio sesion
    if 'usuario_id' not in session:
        return redirect("/") #envia a login
    
    form = {"id": session['usuario_id']}
    usuario = Usuario.obtener_por_id(form)
    
    #ID  del suceso
    data_suceso  ={"id":id}
    #Instancia de receta
    suceso =Suceso.obtener_por_id(data_suceso)

    #COMO EXTRA VERIFICO QUE LA RECETA QUE VOY A EDITAR CORRESPONDA AL USUARIO EN SESSION O SI NO PODRIA A TRAVES DE LA URL ACCEDER A ESTE
    if suceso.usuario_id != session['usuario_id']:
        return redirect("/dashboard")

    return render_template('editar_suceso.html', suceso=suceso, usuario=usuario)


@app.route("/actualizar", methods=["POST"])
def actualizar_suceso():
    #verificar que el usuario inicio sesion
    if 'usuario_id' not in session:
        return redirect("/") #envia a login
    
    #recibimos unrequest.form = {con los datos que actualiza el usuarion en la pagina edit.html}
    #validar que la info de receta es correcta
    if not Suceso.validar_suceso(request.form):
        return redirect("/editar/suceso/"+request.form['id'])
    
    Suceso.actualizar(request.form)
    return redirect("/dashboard")


@app.route('/mostrar/suceso/<int:id>')
def mostrar_suceso(id):
    #verificar que el usuario inicio sesion
    if 'usuario_id' not in session:
        return redirect("/") #envia a login
    
    form = {"id": session['usuario_id']}
    usuario = Usuario.obtener_por_id(form)
    
    #Llamar a un método que en base al ID me regrese una instancia de receta
    data_suceso = {"id": id}
    suceso = Suceso.obtener_por_id(data_suceso)

    data_like = {"usuario_id":session['usuario_id'],
                "suceso_id":id}

    estado = Like.validar_estado_like(data_like)

    usuarios_si = Like.usuarios_sucesos_si()
    usuarios_no = Like.usuarios_sucesos_no()


    return render_template('mostrar_suceso.html', suceso=suceso, usuario=usuario, estado=estado, usuarios_si=usuarios_si,usuarios_no=usuarios_no)

@app.route("/borrar/suceso/<int:id>")
def borrar_suceso(id):
    #verificar que el usuario inicio sesion
    if 'usuario_id' not in session:
        return redirect("/") #envia a login
    
    data_suceso  ={"id":id}
    Like.borrar_likes(data_suceso)
    #metodo que elimine una receta en base al ID
    Suceso.borrar(data_suceso)

    return redirect("/dashboard")
