# import mysql.connector

# mysql_db = mysql.connector.connect(
#     host='localhost',
#     port=3306,
#     user="root",
#     password="fsfal4ever",
#     db="mountainhikedef"
#     )
# mysql_cursor=mysql_db.cursor()

# mysql_cursor.execute("INSERT INTO recorridos (id_recorridos, nombre, descripcion, id_guia, valor) VALUES (4,'Pan de Azúcar','El Pan de Azúcar es un cerro ubicado en la Sierras Chicas, que están al este del Valle de Punilla. Se puede acceder de forma gratuita si se va caminando y se demora un poco menos de 1 hora en alcanzar su cima. Si no se quiere caminar, también está la opción de tomar al aerosilla , aunque pierde un poco la gracia. Si bien el ascenso es muy sencillo, vale la pena llegar hasta la cima para apreciar las increíbles vistas que se tienen del Valle de Punilla, al oeste, y la Ciudad de Córdoba, al este. El sendero está muy bien marcado, así que es fácil orientarse. Además suele ser bastante concurrido, sobre todo en verano, por lo que no vamos a ser los únicos en el camino.', 2, 50000)")

import mysql.connector

class Conectar():
    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port= 3306,
                user= 'root',
                password='fsfal4ever',
                db='mmountainhikedf'                
                )
        except mysql.connector.Error as descripcionError:
            print("No se conectó", descripcionError)
    def InsertarValor(self, id_recorridos, nombre, descripcion, id_guia,valor):
        if self.conexion.is_connected():
            print("conexión exitosa")
            try:
                cursor= self.conexion.cursor()
                sentenciaSQL="INSERT INTO recorridos VALUES (4,'Pan de Azúcar','El Pan de Azúcar es un cerro ubicado en la Sierras Chicas, que están al este del Valle de Punilla. Se puede acceder de forma gratuita si se va caminando y se demora un poco menos de 1 hora en alcanzar su cima. Si no se quiere caminar, también está la opción de tomar al aerosilla , aunque pierde un poco la gracia. Si bien el ascenso es muy sencillo, vale la pena llegar hasta la cima para apreciar las increíbles vistas que se tienen del Valle de Punilla, al oeste, y la Ciudad de Córdoba, al este. El sendero está muy bien marcado, así que es fácil orientarse. Además suele ser bastante concurrido, sobre todo en verano, por lo que no vamos a ser los únicos en el camino.', 2, 50000)"
                data=(id_recorridos, nombre, descripcion, id_guia,valor)
                
                cursor.execute(sentenciaSQL, data)
                self.conexion.commit()
                self.conexion.close()
            except mysql.connector.Error as e:
                print("no se pudo conectar a la base de datos", e)