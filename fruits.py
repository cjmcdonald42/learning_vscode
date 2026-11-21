import sqlite3

with sqlite3.connect("application.db") as connection:
	connection.execute(
		'''
		CREATE TABLE IF NOT EXISTS fruits (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			"Fruit Name" TEXT NOT NULL,
			"Fruit Type" TEXT NOT NULL,
			price REAL NOT NULL
		)
		'''
	)


def add_fruit(fruit_name, fruit_type, price):
	"""Add a fruit record and return its ID."""
	with sqlite3.connect("application.db") as connection:
		cursor = connection.execute(
			'INSERT INTO fruits ("Fruit Name", "Fruit Type", price) VALUES (?, ?, ?)',
			(fruit_name, fruit_type, price),
		)
		return cursor.lastrowid

