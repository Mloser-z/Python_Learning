import pymysql

db = pymysql.connect(host="localhost", user="Mloser", port=613, database="mystudy")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s" % data)
db.close()
