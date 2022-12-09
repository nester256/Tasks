import requests
from time import monotonic
URL = "https://cataas.com/cat"
OUTPUT_FILE = "cats/cat{0}.jpg"

def get_image(url, filename):
    response = requests.get(url, timeout=(5,5))
    if response.status_code != 200:
        return
    else:
        with open(filename, "wb") as file:
            file.write(response.content)

initial = monotonic()
for i in range(10):
    get_image(URL, OUTPUT_FILE.format(i))