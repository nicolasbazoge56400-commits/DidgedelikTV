import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

class FineTuningDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]

class FineTuner:
    def __init__(self, model, train_data, train_labels, learning_rate=1e-4, batch_size=32, num_epochs=10):
        self.model = model
        self.dataset = FineTuningDataset(train_data, train_labels)
        self.dataloader = DataLoader(self.dataset, batch_size=batch_size, shuffle=True)
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = optim.Adam(self.model.parameters(), lr=learning_rate)
        self.num_epochs = num_epochs

    def train(self):
        self.model.train()
        for epoch in range(self.num_epochs):
            for inputs, labels in self.dataloader:
                self.optimizer.zero_grad()
                outputs = self.model(inputs)
                loss = self.criterion(outputs, labels)
                loss.backward()
                self.optimizer.step()
            print(f'Epoch [{epoch + 1}/{self.num_epochs}], Loss: {loss.item():.4f}')

# Example usage
if __name__ == '__main__':
    model = YourPretrainedModel()  # Replace with your model
    fine_tuner = FineTuner(model, train_data, train_labels)
    fine_tuner.train()