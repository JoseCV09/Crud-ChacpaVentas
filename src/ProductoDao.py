import pymysql
from conexion import Conexion
from sqlalchemy import create_engine
from json import dumps
cx = Conexion()

class Producto:
    id_producto = 0
    nombre_producto = ""
    precio = 0
    cantidad = 0
    estado = ""
    def readAll(self):
        try:
            conexion=cx.conecta()
            cursor = conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc('listar_producto')
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print(e)
        finally:
            conexion.close()


    def buscarproducto(self):
        try:
            conexion=cx.conecta()
            cursor=conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc('read_producto',[self.id_producto,])
            rows=cursor.fetchall()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()

    
    def agregarproducto(self):
        nombre_producto=self.nombre_producto
        precio=self.precio
        cantidad=self.cantidad
        data=[nombre_producto, precio, cantidad]
        try:
            conexion=cx.conecta()
            cursor=conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc("create_producto",data)
            conexion.commit()
            return 1
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()


    def deleteproducto(self):
        try:
            conexion=cx.conecta()
            cursor=conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc('delete_producto',[self.id_producto])
            conexion.commit()
            return 1
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()
    
    
    def modificarproducto(self):
        try:
            idp=self.id_producto
            nom_prod=self.nombre_producto
            pre=self.precio
            cant=self.cantidad
            est=self.estado
            data=[nom_prod,pre,cant,est,idp]
            conexion=cx.conecta()
            cursor=conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc("update_producto",data)
            conexion.commit()
            return 1
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()