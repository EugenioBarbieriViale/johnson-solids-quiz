from os import path
import pandas as pd
from random import randint
import solids



dirname = "data/"

f1 = dirname + "names.csv"
f2 = dirname + "image_urls.csv"

w = solids.Solids()

if not path.isfile(f1):
    names = w.get_names()
    w.save(f1, names)
    print("Names saved to file", f1)

if not path.isfile(f2):
    im = w.get_image_urls()
    w.save(f2, im)
    print("URLs saved to file", f2)
    
names = pd.read_csv(f1).values
img_urls = pd.read_csv(f2).values


index = randint(0, 91)

print(names[index][0])
img = w.open_image(img_urls[index][0])
