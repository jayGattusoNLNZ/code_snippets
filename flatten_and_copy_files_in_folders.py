import os
import stat
import errno
import shutil
from pathlib import Path
import hashlib

def file_hash(filename):
  h = hashlib.sha256()
  with open(filename, 'rb', buffering=0) as f:
    for b in iter(lambda : f.read(128*1024), b''):
      h.update(b)
  return h.hexdigest()

def handleRemoveReadonly(func, path, exc):
  excvalue = exc[1]
  if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
      os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
      func(path)
  else:
      raise


source = Path(r"C:\Users\gattusoj\Desktop\COPY_DA_2015_Phillip Mann_A2015-018")
destination = Path(r"D:\flat_foldering_copier\phillip_mann_2")


stopfiles = ["_da_logfile_.csv",
				"_da_logfile.csv",
				"_DA_logfile.csv",
				"_DA_logfile.csv",
				"_da_logfile_2.csv",
				"_da_logfile_1.csv",
				"_DA_BC_logfile.csv",
				"_da_logfile_1_1381-1388.csv",
				"FILEID.DAT",
				"FINDER.DAT",
				"OpenFolderListDF",
				"OpenFolderListDF_",
				"hash.csv",
				"Temporary Items",
				"Trash",
				"Desktop Folder",
				"DESKTOP",
				"Desktop"]


# try:
# 	if os.path.exists(destination):
# 		shutil.rmtree(destination, ignore_errors=False, onerror=handleRemoveReadonly)
# except:
# 	print ("Can't delete existing move attempt - please delete {} manually if you need a clean copy".format(destination))


if not os.path.exists(destination):
	os.mkdir(destination)

for root, subs, files in os.walk(source):
	#### process only files that we think we want 
	#### having added the ones one don't to the stop list.... 
	for f in  [x for x in files if x not in stopfiles]: 
		#### make the current filepath object
		my_file_path = Path(root)/f
		
		### if this file doesn't exist already, do this part
		if not os.path.exists(destination/f):

			shutil.copy(my_file_path, destination)
			### trying to handle the permission issue that cropped up... 
			try:
				print (shutil.copy2(my_file_path, destination/f))
				if not file_hash(my_file_path) == file_hash(destination/f):
					print ("Failed on fixity : {}".format(my_file_path))
			except PermissionError:
				print ("Struggling with: {}".format(my_file_path))
				quit()
		#### if there is a file of that filenmame in the destination folder then this branch happens. 
		else:
			if not file_hash(my_file_path) == file_hash(destination/f):
				new_file_path = ""
				counter = 0
				while True: 
					counter += 1					
					new_file_path = destination/"{}_({}){}".format(my_file_path.stem, counter, my_file_path.suffix)  
					if not os.path.exists(new_file_path):
						shutil.copy(my_file_path, new_file_path)
						break





