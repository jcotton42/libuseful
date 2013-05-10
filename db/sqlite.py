import sqlite3
class DatabaseConnection():
	"""
	This class represents a connection to a SQLite3 database.
	You can query the database or update it.
	"""
	def __init__(self, filename):
		self.db = sqlite3.connect(filename)
	def query(self, query, args=(), one=False):
		"""
		Query the database. Returns a list of dictionaries;
		each column repesenting a key in the dictionary.
		Example:
		>>> conn = DatabaseConnection("example.db")
		>>> res = conn.query("select * from example", one=True)
		>>> res["age"]
		13
		>>> res["name"]
		u'Fox Wilson'
		"""
		cur = self.db.execute(query, args)
		r = [dict((cur.description[idx][0], value)
			for idx, value in enumerate(row)) for row in cur.fetchall()
			]
		if not one: return r
		return r[0] if r else None
	def execute(self, query, args=()):
		"""
		Execute a command on the database. All this does is
		remove the need for a seperate commit on the
		database.
		"""
		self.db.execute(query, args)
		self.db.commit()
if __name__ == "__main__":
	import doctest
	doctest.testmod()
