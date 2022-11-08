import mysql.connector

mybbdd= mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password= "fsfal4ever",
    db="mountainhikedef"
)
mycursor= mybbdd.cursor()
mycursor.execute("use recorridos;")
datos="INSERT INTO recorridos('id_recorridos', 'nombre', 'descripcion', 'id_guia','valor') values (4,'Pan de Azúcar','El Pan de Azúcar es un cerro ubicado en la Sierras Chicas, que están al este del Valle de Punilla. Se puede acceder de forma gratuita si se va caminando y se demora un poco menos de 1 hora en alcanzar su cima. Si no se quiere caminar, también está la opción de tomar al aerosilla , aunque pierde un poco la gracia. Si bien el ascenso es muy sencillo, vale la pena llegar hasta la cima para apreciar las increíbles vistas que se tienen del Valle de Punilla, al oeste, y la Ciudad de Córdoba, al este. El sendero está muy bien marcado, así que es fácil orientarse. Además suele ser bastante concurrido, sobre todo en verano, por lo que no vamos a ser los únicos en el camino.', 2, 50000);"
mycursor.execute(datos)
mycursor.execute("select * from recorridos;")




