import os
import shutil
import tarfile

##### edit these two lines only #####
source = r"Y:\DPS_Export-prod\gattusoj\export\towmey"
destination = r"D:\finale_files\collection"
#####################################

for item in os.listdir(source):
	item_path = os.path.join(source, item)
	try:
		os.remove(os.path.join(item_path, "ie.xml"))
	except FileNotFoundError:
		pass
	for rep in os.listdir(item_path):
		for my_file in os.listdir(os.path.join(item_path, rep)):
			my_file_path = os.path.join(item_path, rep, my_file)
			new_file_destination = my_file_path.replace(os.path.join(item_path, rep), destination)
			shutil.copy2(my_file_path, new_file_destination)
			tar = tarfile.open(new_file_destination, "r:")
			tar.extractall(destination)
			tar.close()
			os.remove(new_file_destination)

