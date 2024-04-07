from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash #es el encargado de mostrar errores


class Like:

    def __init__(self,data):
        #data(diccionario): {"id": 1, "nombre": "Elena", "apellido": "De troya",.....}
        self.id = data['id']
        self.usuario_id = data['usuario_id']
        self.suceso_id = data['suceso_id']
        self.estado = data['estado']

        #JOIN
        #self.nombre_usuario = data["nombre_usuario"]

    @staticmethod
    def validar_like(form):
        #form = {diccionario con todos los valores que el usuario ingreso}
        is_valid = True #asume que todos los valores cumplen con los requisitos

        #validamos que el like existe o no
        query = "SELECT * FROM likes WHERE usuario_id = %(usuario_id)s and suceso_id = %(suceso_id)s"
        results = connectToMySQL('ovnis').query_db(query,form)
        if len(results) >= 1:
            print("like existente")
            is_valid=False

        return is_valid

    @classmethod #OOK OKO KO KO KO KOK
    def guardar_like(cls,form):
        
        #formulario = {"id": 1, "usuario_id": "Elena", "descripcion": "De Troya","fecha": "elena@codingdojo.com","ovnis": YA ENCRIPTADA}
        query = "INSERT INTO likes (usuario_id, suceso_id,estado) VALUES (%(usuario_id)s,%(suceso_id)s, %(estado)s)"
        result = connectToMySQL('ovnis').query_db(query,form) # Id del nuevo registro que se crea
        return result
    
    @classmethod
    def actualizar_like(cls, form):
        # form  = request.form
        query = "UPDATE likes SET estado = %(estado)s WHERE usuario_id = %(usuario_id)s and suceso_id = %(suceso_id)s"
        result  =connectToMySQL('ovnis').query_db(query, form)
        return result

    @classmethod
    def validar_estado_like(cls,form):
        #form {"id": 1}
        query = "SELECT * FROM likes WHERE usuario_id = %(usuario_id)s and suceso_id = %(suceso_id)s"
        results = connectToMySQL('ovnis').query_db(query,form)#lista de diccionarios que en realidad es solo un diccionario con posicion 0
        
        estado = 0
        
        if len(results) < 1:
            estado = 0
            print( "estado 0000")
        else:
            like = cls(results[0])
            if like.estado == "si":
                estado = 1
                print( "estado 1111")
            elif like.estado == "no":
                print( "estado 2222")
                estado = 2

        return estado 

    @classmethod
    def borrar_likes(cls, data):
        query = "DELETE FROM likes WHERE suceso_id = %(id)s"
        result=connectToMySQL('ovnis').query_db(query, data)
        return result

    @staticmethod
    def cant_si():
        query = "SELECT suceso_id, COUNT(*) AS cantidad_si FROM likes WHERE estado = 'si' GROUP BY suceso_id ORDER BY suceso_id"
        results  = connectToMySQL('ovnis').query_db(query)
        return results 
    
    @staticmethod
    def cant_no():
        query = "SELECT suceso_id, COUNT(*) AS cantidad_no FROM likes WHERE estado = 'no' GROUP BY suceso_id ORDER BY suceso_id"
        results  = connectToMySQL('ovnis').query_db(query)
        return results 
    
    @staticmethod
    def usuarios_sucesos_si():
        query = "SELECT usuarios.nombre AS nombre_usuario, sucesos.id AS suceso_id FROM usuarios JOIN likes ON usuarios.id = likes.usuario_id JOIN sucesos ON likes.suceso_id = sucesos.id WHERE likes.estado = 'si' ORDER BY suceso_id"
        results = connectToMySQL('ovnis').query_db(query)
        return results
    
    @staticmethod
    def usuarios_sucesos_no():
        query = "SELECT usuarios.nombre AS nombre_usuario, sucesos.id AS suceso_id FROM usuarios JOIN likes ON usuarios.id = likes.usuario_id JOIN sucesos ON likes.suceso_id = sucesos.id WHERE likes.estado = 'no' ORDER BY suceso_id"
        results = connectToMySQL('ovnis').query_db(query)
        return results


