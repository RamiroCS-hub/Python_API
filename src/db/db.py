from flask import g
import sqlite3

DATABASE = 'database.db'
def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
	return db

def close_db ():
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()

def clean_database(db):
	tables = ["Choises", "Situations", "Choises_Situations"]
	for table in tables:
		db.execute(f"DROP TABLE IF EXISTS {table}")
	db.commit()

def init_db():
	from app import app
	from db.seed import Seeder 
	with app.app_context():
		seed = Seeder()
		db = get_db()
		# Abre la base de datos en modo lectura y ejecuta el script que esta dentro
		clean_database(db)
		with app.open_resource('db\schema.sql', mode='r') as f:
				db.cursor().executescript(f.read())
		db.commit()
		seed.seed_situations()
		seed.seed_choises()
		seed.seed_choises_situations()
