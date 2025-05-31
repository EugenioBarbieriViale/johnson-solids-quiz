import requests
from bs4 import BeautifulSoup
from csv import writer
import io
# import matplotlib.pyplot as plt
from time import sleep


class Solids:
    def __init__(self):
        self.url = "https://en.wikipedia.org/wiki/List_of_Johnson_solids"

        self.headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        self.s = requests.Session()
        self.r = self.s.get(self.url, headers=self.headers)

        self.soup = BeautifulSoup(self.r.content, "html.parser")

    def get_names(self):
        all_td = self.soup.find_all("td")

        names = []
        for t in all_td:
            a = t.a
            if a is not None and "href" in a.attrs and "title" in a.attrs:
                if a.text[0].isupper():
                    names.append([a.text])

        return names

    def get_images(self):
        all_img = self.soup.find_all("img", class_="mw-file-element")

        images = []
        for a in all_img:
            if "commons" in a["src"]:
                img_url = "https:" + a["src"]

                img_url = img_url.replace("thumb/", "")
                img_url = img_url.split("/120", 1)[0]

                print(img_url)
                response = requests.get(img_url, stream = True)
                sleep(5)
                
                if response.status_code != 200:
                    print(f"! Failed to download {img_url} (HTTP {response.status_code})")

                img = plt.imread(io.BytesIO(response.content), format="PNG")

                images.append([img])


        return images

    def get_image_urls(self):
        all_img = self.soup.find_all("img", class_="mw-file-element")

        img_urls = []
        for a in all_img:
            if "commons" in a["src"]:
                img_url = "https:" + a["src"]

                img_url = img_url.replace("thumb/", "")
                img_url = img_url.split("/120", 1)[0]

                img_urls.append(img_url)

        return img_urls

    def open_image(self, img_url):
        response = requests.get(img_url, stream = True)
        
        if response.status_code != 200:
            print(f"! Failed to download {img_url} (HTTP {response.status_code})")

        img = io.BytesIO(response.content)
        return img

    def save(self, file_path, array):
        with open(file_path, mode="w", newline="") as file:
            w = writer(file)
            w.writerows(array)
