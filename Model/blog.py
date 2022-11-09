import pymysql


connection= pymysql.connect(
    host='localhost',
    user='root',
    passwd= 'fsfal4ever',
    db='mountainhikedef', 
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
try:
    with connection.cursor() as cursor:
        sql = "UPDATE blog SET fecha= '1 de enero' WHERE id_blog = 1;"
        cursor.execute(sql)
        connection.commit()
    
finally:
    connection.close()
