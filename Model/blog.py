# import mysql.connector

# class Conectar():
# 	def init(self) -> None: 
# 	    try:
# 		self.conexion = mysql.connector.connect(
# 		    host = 'localhost',
# 		    port = 3306,
# 		    user = 'root',
# 		    password = 'ContraseñaBBDD',
# 		    db = 'MiBaseDeDatos'
# 		)
# 	     except mysql.connector.Error as descripcionError:
# 		print("¡No se conectó!",descripcionError)

# 	#1
# 	def InsertarValor(self, nombre, telefono, direccion):
# 	    if self.conexion.is_connected():
# 		try:
# 		    cursor = self.conexion.cursor()
# 		    sentenciaSQL = "INSERT INTO tablaDeEjemplo VALUES(%s,%s,%s)"
# 		    data = (nombre, telefono, direccion)

# 		    cursor.execute(sentenciaSQL,data)
# 		    self.conexion.commit()
# 		    self.conexion.close()
		    
# 		except:
# 		    print("No se pudo conectar a la base de datos")

# 	#2
# 	def BuscarObjeto(self,nombre):
# 	    if self.conexion.is_connected():
# 		try:
# 		    cursor = self.conexion.cursor()
# 		    sentenciaSQL = "SELECT* from tablaDeEjemplo where nombre like '%MAR%'"
		    
# 		    cursor.execute(sentenciaSQL)
# 		    resultadoREAD = cursor.fetchall()
# 		    self.conexion.close()
# 		    return resultadoREAD

# 		except:
# 		    print("No se pudo conectar a la base de datos")

# 	#3
# 	def InsertarValor(self, ID, nombre, telefono, direccion):
# 	    if self.conexion.is_connected():
# 		try:
# 		    cursor = self.conexion.cursor()
# 		    sentenciaSQL = "UPDATE tablaDeEjemplo VALUES(%s,%s,%s)"
# 		    data = (nombre, telefono, direccion)

# 		    cursor.execute(sentenciaSQL)
# 		    self.conexion.commit()
# 		    self.conexion.close()
		    
# 		except:
# 		    print("No se pudo conectar a la base de datos")

# 	#4
# 	def EliminarObjeto(self,ID):
#             if self.conexion.is_connected():
#                 try:
#                     cursor = self.conexion.cursor()
#                     sentenciaSQL = "DELETE from tablaDeEjemplo where id = ID"
#                     cursor.execute(sentenciaSQL)

#                     self.conexion.commit()                
#                     self.conexion.close()

#                 except:
#                     print("No se pudo concectar a la base de datos")