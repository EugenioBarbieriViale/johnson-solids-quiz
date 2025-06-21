from os import path, mkdir
import pandas as pd
from random import randint

import webscrape
import neural_network

dirname = "data/"

f1 = dirname + "names.csv"
f2 = dirname + "image_urls.csv"
imgs_dir = dirname + "images/" # remember to put / at the end

w = webscrape.Webscrape()

if not path.isfile(f1):
    names = w.get_names()
    w.save(f1, names)
    print("Names saved to file", f1)

if not path.isfile(f2):
    urls = w.get_image_urls()
    w.save(f2, urls)
    print("URLs saved to file", f2)

if not path.isdir(imgs_dir):
    mkdir(imgs_dir)
    w.download_images(imgs_dir)
    print("Images downloaded to directory:", imgs_dir)
    
names = pd.read_csv(f1).values.flatten()
# index = randint(0, 91)

# w.open_image_file(names[index], imgs_dir)

nn = neural_network.JS_Classifier()
nn.learn(epochs=10, filename="model.pth")
