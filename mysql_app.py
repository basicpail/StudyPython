import MySQLdb

db = MySQLdb.connect(host = '210.119.12.52',\
                     user = 'test_usr',\
                     password = 'mysql_p@ssw0rd',\
                     database = 'shopdb',\
                     charset='utf8')

cur = db.cursor()

#db.query("set character_set_connection=utf8;")
#db.query("set character_set_server=utf8;")
#db.query("set character_set_client=utf8;")
#db.query("set character_set_results=utf8;")
#db.query("set character_set_database=utf8;")

#query = "SQL Sentence"
#cur.execute("set names utf8")
cur.execute('select * from producttbl')

while True:
    product = cur.fetchone()
    if not product:
        break

    print(product)

cur.close()
db.close()