#importaciones
from flask import Flask, render_template, request, redirect, session, flash

#importar la app
from flask_app import app

#importar todos los modelos
from flask_app.models.sucesos import Suceso
from flask_app.models.usuarios import Usuario
from flask_app.models.likes import Like



#Rutas
@app.route('/like', methods=["POST"])
def like():
    #verificar que el usuario inicio sesion
    if 'usuario_id' not in session:
        return redirect("/")
    
    #validar si el like existe
    #si el like no existe..ejecutar
    #esto pregunta si esta vacio el like
    if not Like.validar_like(request.form):
        Like.actualizar_like(request.form)
    else:
        Like.guardar_like(request.form)
        return redirect("/dashboard")
    
    return redirect("/dashboard")


