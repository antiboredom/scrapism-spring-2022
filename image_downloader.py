import requests
from bs4 import BeautifulSoup

def download_file(url, local_filename=None):
    if local_filename is None:
        local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)

# download_file("https://image.shutterstock.com/z/stock-photo-young-hispanic-man-wearing-police-uniform-covering-eyes-with-hands-and-doing-stop-gesture-with-sad-1907730751.jpg", "sadcop.jpg")

base_url = "https://lav.io"
response = requests.get(base_url)
soup = BeautifulSoup(response.text, "html.parser")
images = soup.select("img")
for i in images:
    image_url = base_url + i.attrs.get('src')
    print(image_url)
    download_file(image_url)