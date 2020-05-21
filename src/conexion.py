
import pymysql
class Conexion:
    def __init__(self):
        self._HOST = "bgqzoxqrfr1odrejhzeu-mysql.services.clever-cloud.com"
        self._USER = "uu0uxvt2ck4xkfqf"
        self._PASS = "W1Y8FYfQSVR7KIwWnUlZ"
        self._BD = "bgqzoxqrfr1odrejhzeu"
    def conecta(self):
        bd = pymysql.connect(self._HOST, self._USER, self._PASS, self._BD, port=3306)
        print("Conexion Exitosa...!")
        return bd
cx = Conexion()
print(cx.conecta())