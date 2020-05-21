import pymysql
from conexion import Conexion
from sqlalchemy import create_engine
from json import dumps
cx = Conexion()

class Cliente:
    id_cliente = 0
    nombre_cliente = ""
    apellido_cliente = ""
    dni = ""
    correo = ""
    direccion = ""
    telefono = ""
    def readAll(self):
        try:
            conexion=cx.conecta()
            cursor = conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc('listar_cliente')
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print(e)
        finally:
            conexion.close()


    def buscarcliente(self):
        try:
            conexion=cx.conecta()
            cursor=conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc('read_cliente',[self.id_cliente,])
            rows=cursor.fetchall()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()

    
    def agregarcliente(self):
        nombre_cliente=self.nombre_cliente
        apellido_cliente=self.apellido_cliente
        dni=self.dni
        correo=self.correo
        direccion=self.direccion
        telefono=self.telefono
        data=[nombre_cliente, apellido_cliente, dni,correo,direccion,telefono]
        try:
            conexion=cx.conecta()
            cursor=conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc("create_cliente",data)
            conexion.commit()
            return 1
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()


    def deletecliente(self):
        try:
            conexion=cx.conecta()
            cursor=conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc('delete_cliente',[self.id_cliente])
            conexion.commit()
            return 1
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()
    
    
    def modificarcliente(self):
        try:
            idc=self.id_cliente
            nom_cliente=self.nombre_cliente
            ape_cliente=self.apellido_cliente
            dni2=self.dni
            correo2=self.correo
            direccion2=self.direccion
            telefono2=self.telefono
            data=[nom_cliente,ape_cliente,dni2,correo2,direccion2,telefono2,idc]
            conexion=cx.conecta()
            cursor=conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc("update_cliente",data)
            conexion.commit()
            return 1
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()