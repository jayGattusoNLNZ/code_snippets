import os
import shutil
import tarfile
import pickle

##### edit these two lines only #####
source = r"K:\cartes_de_visites"
destination = r"K:\cartes_de_visites_unpacked"
#####################################

if not os.path.exists(destination):
	os.makedirs(destination)

data = []
files_list = os.listdir(source)
for item in os.listdir(source):
	item_path = os.path.join(source, item)
	try:
		os.remove(os.path.join(item_path, "ie.xml"))
	except FileNotFoundError:
		pass
	for rep in os.listdir(item_path):
		for my_file in os.listdir(os.path.join(item_path, rep)):
			my_file_path = os.path.join(item_path, rep, my_file)
			tar = tarfile.open(my_file_path, "r:")
			files = tar.getnames()
			for f in files:
				with open("files_in_tar.txt", "a") as data:
					print (my_file_path)
					print (f)
					data.write(("{}|{}\n").format(my_file_path, f))
