#import sqlite3
#def create_db():
#	con=sqlite3.connect(database=r'ims.db')
#	cur=con.cursor()
#	cur.execute("CREATE TABLE IF NOT EXISTS users(uid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,passwd text,utype text,salary text,address text)")
#	con.commit()
#create_db()


##===================================================================================##
import sqlite3
def create_db():
	con=sqlite3.connect(database=r'databases/system.db')
	cur=con.cursor()
	cur.execute("""CREATE TABLE IF NOT EXISTS users(
			uid INTEGER PRIMARY KEY AUTOINCREMENT,
			name text,
			email text,
			gender text,
			contact integer,
			dob text,
			doj text,
			passwd text,
			utype text,
			salary integer,
			address text
				)""")
	con.commit()
create_db()
