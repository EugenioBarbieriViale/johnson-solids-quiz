import os
from numpy import array
from pandas import read_csv
from cv2 import imread, resize, INTER_AREA

import torch
import torchvision.transforms

class JS_Dataset(torch.utils.data.Dataset):
    def __init__(self, data_path="data/images", labels_path="data/names.csv"):
        super().__init__()

        transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])

        imgs = []
        for root, sub, file in os.walk(path):
            for f in file:
                filepath = os.path.join(root, f)
                img = imread(filepath, 0) # 0 is grayscale

                img = resize(img, (64, 64), interpolation=INTER_AREA)
                imgs.append(img)

        self.dataset = array(imgs)
        self.labels = read_csv(labels_path).values.flatten()

    def __getitem__(self, index):
        x = self.dataset[index]
        y = self.labels[index]

        return transform(x), transform(y)
    
    def __len__(self):
        return len(self.dataset)
