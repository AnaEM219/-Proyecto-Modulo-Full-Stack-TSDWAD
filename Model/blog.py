import pymysql
print("resultado exitoso")

class Blog():
    
    def __init__(self)-> None:
        try:
            self.mybbdd= pymysql.connect(
                host='localhost',
                user='root',
                passwd= "fsfal4ever",
                db="mountainhikedef"
                )
        except pymysql.Error as descriptionerror:
            print("No se conectó", descriptionerror)
    def InsertarValor(self):
        if self.mybbdd.conn.ping(True):
            try:
                mycursor= self.mybbdd.cursor()                 
                mycursor.execute("SELECT fecha, titulo FROM blog")
                for fecha, titulo in mycursor.fetchall():
                    print (fecha, titulo)
                self.mybbdd.close()
            except ConnectionError:
                print("No se pudo jsdfklj")