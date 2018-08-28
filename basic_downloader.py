import requests
import os

url = ""
destination_folder = ""

def download_file(url):
    local_filename = os.path.join(destination_folder, url.split('/')[-1])
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)
    return local_filename

download_file(url)