from csv import writer
from os import path
import matplotlib.pyplot as plt
import pandas as pd
from random import randint, shuffle
from PIL import Image

import webscrape

dirname = "data/"

f1 = dirname + "names.csv"
f2 = dirname + "images.csv"

w = webscrape.Solids()

if not path.isfile(f1):
    names = w.get_names()
    w.save(f1, names)
    print("Names saved to file", f1)

# if not path.isfile(f2):
#     images = w.get_images()
#     w.save(f2, images)
#     print("Images saved to file", f2)
    
names = pd.read_csv(f1).values
img_urls = w.get_image_urls()
# images = pd.read_csv(f2).values

while True:
    index = randint(0, 92)

    # print(names[index][0])
    img = w.open_image(img_urls[index])

    # img = plt.imread(img, format="PNG")
    img = Image.open(img)
    plt.imshow(img)
    plt.show()

    options = [names[index-1][0], names[index][0], names[index+1][0]]
    options.shuffle()

    print("A)", options[0])
    print("B)", options[1])
    print("C)", options[2])

    inp = str(input("Answer: "))
    if inp == "A" and options[0] == names[index][0]:
        print("Correct!")
    elif inp == "B" and options[1] == names[index][0]:
        print("Correct!")
    elif inp == "C" and options[2] == names[index][0]:
        print("Correct!")
    else:
        print("Wrong, the answer is", names[index][0])

    print("-----------------------------------------")
