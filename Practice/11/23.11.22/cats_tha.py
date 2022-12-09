# Коты потоками
from threading import Thread
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

if __name__ == '__main__':
    threads = []
    initial = monotonic()
    for i in range(10):
       thread = Thread(target=get_image, args=(URL, OUTPUT_FILE.format(i)))
       thread.start()
       threads.append(thread)

    for thread in threads:
        thread.join()

    print("Time: ", monotonic() - initial)