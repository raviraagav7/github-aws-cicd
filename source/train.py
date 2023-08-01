import torch.optim as optim
from data import load_data
from model import *
import os

def train_model(dataloader):
    # Set up the device (CPU or GPU)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Create an instance of the model
    net = Net().to(device)

    # Define the loss function and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

    # Train the model
    for epoch in range(20):
        running_loss = 0.0
        for i, data in enumerate(dataloader, 0):
            inputs, labels = data[0].to(device), data[1].to(device)

            optimizer.zero_grad()
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            if i % 2000 == 1999:
                print('[%d, %5d] loss: %.3f' % (epoch + 1, i + 1, running_loss / 2000))
                running_loss = 0.0

    print('Training finished.')
    torch.save(net.state_dict(), f'{os.path.pardir}/test/model.pt')

if __name__ == '__main__':
    dataloader = load_data('train')
    train_model(dataloader=dataloader)


