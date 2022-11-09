import pymysql


connection= pymysql.connect(
    host='localhost',
    user='root',
    passwd= 'fsfal4ever',
    db='mountainhikedef', 
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)






