from os import path

import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

from dataloader import JS_Dataset


class JS_Classifier(JS_Dataset):
    def __init__(self):
        super().__init__()

        data = JS_Dataset()
        self.train = torch.utils.data.DataLoader(
            data,
            batch_size = 4,
            shuffle = True
        )

        self.device = "cpu"
        self.model = self.NN().to(self.device)

        self.loss_fn = nn.CrossEntropyLoss()
        self.optimizer = torch.optim.SGD(self.model.parameters(), lr = 1e-3)

    def train(self):
        size = self.train.dataset.len()
        self.model.train()

        for self.batch, (x, y) in enumerate(self.train):
            x, y = x.to(self.device), y.to(self.device)

            # Compute prediction error
            pred = self.model(x)
            loss = self.loss_fn(pred, y)

            # Backpropagation
            loss.backward()
            self.optimizer.step()
            self.optimizer.zero_grad()

            # if self.batch % 100 == 0:
            loss, current = loss.item(), (self.batch + 1) * len(x)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")

    def learn(self, epochs=10, filename="model.pth"):
        if not path.isfile(filename):
            for i in range(epochs):
                print(f"Epoch {i+1}\n-------------------------------")
                self.train()

            print("Training finished!")

            torch.save(self.model.state_dict(), filename)
            print("Model saved to", filename)

    class NN(nn.Module):
        def __init__(self):
            super().__init__()

            self.flatten = nn.Flatten()
            self.stack = nn.Sequential(
                nn.Linear(64*64, 2048),
                nn.ReLU(),
                nn.Linear(2048, 512),
                nn.ReLU(),
                nn.Linear(512, 92),
            )

        def forward(self, x):
            x = self.flatten(x)
            x = self.stack(x)
            return x
