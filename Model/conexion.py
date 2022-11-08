import pymysql
print("resultado exitoso")

mybbdd= pymysql.connect(
    host='localhost',
    user='root',
    passwd= "fsfal4ever",
    db="mountainhikedef"
)
mycursor= mybbdd.cursor()
mycursor.execute("SELECT fecha, titulo FROM blog")
for fecha, titulo in mycursor.fetchall():
    print (fecha, titulo)
mybbdd.close()




