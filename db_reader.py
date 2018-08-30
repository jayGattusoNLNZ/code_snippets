import sqlite3

class Db_Tools(object):
	"""makes a per collection db
	var local is for just making the db file in a local sub folder, if false makes on given path
	var flush is for starting over from deployment - mainly for testing 

	http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html#inserting-and-updating-rows
	"""
	def __init__(self):
		"""Manages the sql lite database connection and functions"""
		"""flush is used to manage a complete reset of move. If set, it deletes any existing db file
		and starts the move process from the beginning.
		It should typically be set to false (per the default) for normal operation"""
		"""The local var is used to manage the location of the db file. There is no logic yet for dealing with 
		a db file that isn't local to the script (i.e. the db files will be made in a sub folder of the folder
		safemover is run from)"""
		
		self.conn = None
		self.c = None
		self.setup_db_connect()

	def setup_db_connect(self):
		""" makes the db file if not exists
		supports local/relative assignation, and absolute"""
		self.conn = sqlite3.connect(r"Y:\NDHA_pre-deposit\jay\format_validation_errors\filepids.db")
		self.c = self.conn.cursor()
		# self.db_path = os.path.join("collections_dbs", '{}.db'.format(self.collection_name))





def main():
	my_db = Db_Tools()

	my_db.c.execute('''SELECT * FROM fl_details ''')
	my_files = my_db.c.fetchall()
	print (len(my_files))
	for item in my_files:
		print (item)

		quit()


if __name__ == '__main__':
	main()