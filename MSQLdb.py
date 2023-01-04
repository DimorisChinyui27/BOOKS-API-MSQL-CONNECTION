import pymysql
#PERFECTED IMPLEMENTATION OF API IF YOU FORGET HOW THE CODE WORKS CONVERT EVERY INSTANCE OF BOOK TABLE TO BOOKI IN BOTH SCRIPTS
conn = pymysql.connect(host='sql7.freesqldatabase.com',database='sql7580274',user='sql7580274',password='fJXubzwYfd', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

cursor = conn.cursor()

sql_query  = """CREATE TABLE book (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    author TEXT NOT NULL,
    language TEXT NOT NULL,
    title TEXT NOT NULL
)"""

cursor.execute(sql_query)
conn.close()