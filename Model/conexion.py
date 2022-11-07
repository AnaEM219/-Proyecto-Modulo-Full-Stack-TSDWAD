import mysql.connector

class Conectar():
    def __init__(self)-> None:
        try:
            self.conexion= mysql.connector.connect(
                host= 'localhost',
                user='root',
                password='fsfal4ever',
                db='mountainhikedef'
                )
        except my