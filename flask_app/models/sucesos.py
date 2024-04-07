from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash #es el encargado de mostrar errores


class Suceso:

    def __init__(self,data):
        #data(diccionario): {"id": 1, "nombre": "Elena", "apellido": "De troya",.....}
        self.id = data['id']
        self.lugar = data['lugar']
        self.descripcion = data['descripcion']
        self.fecha = data['fecha']
        self.ovnis = data['ovnis']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.usuario_id = data['usuario_id']

        #JOIN, luego de hacer el join, la nueva variable la llamo de esta forma y la agrego a las variables de clase
        self.nombre_usuario = data["nombre_usuario"]

    @classmethod
    def guardar(cls,form):
        #formulario = {"id": 1, "lugar": "Elena", "descripcion": "De Troya","fecha": "elena@codingdojo.com","ovnis": YA ENCRIPTADA}
        query = "INSERT INTO sucesos (lugar, descripcion, fecha, ovnis,usuario_id) VALUES (%(lugar)s,%(descripcion)s, %(fecha)s,%(ovnis)s,%(usuario_id)s)"
        result = connectToMySQL('ovnis').query_db(query,form) # Id del nuevo registro que se crea
        return result

    @staticmethod
    def validar_suceso(form):
        #form = {diccionario con todos los valores que el usuario ingreso}
        is_valid = True #asume que todos los valores cumplen con los requisitos

        #Validar que el lugar tenga al menos 2 caracteres
        if len(form["lugar"]) < 2:
            flash("Lugar debe tener al menos 2 cracteres", "suceso_validar")
            is_valid = False

        #Validar que la descripcion tenga al menos 2 caracteres
        if len(form["descripcion"]) < 2:
            flash("Descripcion debe tener al menos 2 cracteres", "suceso_validar")
            is_valid=False
        
        if form['fecha'] == "":
            is_valid = False
            flash("Ingresa una fecha de creacion", "suceso_validar")

        if form['ovnis'] == "":
            is_valid = False
            flash("Ingresa la cantidad de ovnis", "suceso_validar")

        return is_valid
    
        
    @classmethod
    def obtener_por_id(cls,data):
        #data {"id": 1}
        query = "SELECT sucesos.* , usuarios.nombre as nombre_usuario FROM sucesos JOIN usuarios ON sucesos.usuario_id = usuarios.id WHERE sucesos.id = %(id)s"
        results = connectToMySQL('ovnis').query_db(query,data)#lista de diccionarios que en realidad es solo un diccionario con posicion 0
        suceso = cls(results[0])
        return suceso 
    
    @classmethod #####pendienteeee
    def obtener_todos(cls):
        query = "SELECT sucesos.* , usuarios.nombre as nombre_usuario FROM sucesos JOIN usuarios ON sucesos.usuario_id = usuarios.id"
        results = connectToMySQL('ovnis').query_db(query) #Lista de diccionarios
        sucesos =[] #aqui se van guardando todas las recetas
        for suceso in results:
            #suceso = {diccionario que recibo de bd - registro columnas}
            sucesos.append(cls(suceso)) # cls(recipe) --> Genera la instancia en base al diccionario. recipes.append --> agrega esa instancia a la lista de recipes
        return sucesos

    @classmethod
    def actualizar(cls, form):
        # form  = request.form
        query = "UPDATE sucesos SET lugar = %(lugar)s, descripcion = %(descripcion)s, fecha = %(fecha)s, ovnis = %(ovnis)s WHERE id  = %(id)s"
        result  =connectToMySQL('ovnis').query_db(query, form)
        return result

    
    @classmethod
    def borrar(cls, data):
        query = "DELETE FROM sucesos WHERE id = %(id)s"
        result=connectToMySQL('ovnis').query_db(query, data)
        return result
    



