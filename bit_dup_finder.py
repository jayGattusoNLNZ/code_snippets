import os
import hashlib
from functools import partial

source = r"D:\finale_files\collection"

def md5sum(filename):
    with open(filename, mode='rb') as f:
        d = hashlib.md5()
        for buf in iter(partial(f.read, 128), b''):
            d.update(buf)
    return d.hexdigest()



master_dict = {}

for root, subs, files in os.walk(source):
	for f in files:
		f_path = os.path.join(root, f)
		f_md5 = (md5sum(f_path)) 

		if f_md5 not in master_dict:
			master_dict[f_md5] = []
		master_dict[f_md5].append(f_path)

for md5, files in master_dict.items():
	if len(files) > 1:
		print (md5)
		for f in files:
			print (f)
			
		print ()
