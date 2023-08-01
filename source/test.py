import os
from source.model import *
from source.data import load_data

def test_model(dataloader, path):
    # Set up the device (CPU or GPU)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Create an instance of the model
    net = Net().to(device)
    net.load_state_dict(torch.load(path))
    net.eval()

    # Evaluate the model on the test dataset
    correct = 0
    total = 0
    with torch.no_grad():
        for data in dataloader:
            images, labels = data[0].to(device), data[1].to(device)
            outputs = net(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    accuracy = 100 * correct / total
    print('Accuracy on the test set: %.2f %%' % accuracy)

if __name__ == '__main__':
    dataloader = load_data('test')
    test_model(dataloader, f'{os.path.pardir}/test/model.pth')
