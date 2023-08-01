import torch
import torchvision
import torchvision.transforms as transforms


def load_data(phase='train'):
    if phase == 'train':
    # Define the transformation to apply to the images
        transform = transforms.Compose([
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ])
        # Load the CIFAR10 training dataset
        trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                                download=False, transform=transform)
        loader = torch.utils.data.DataLoader(trainset, batch_size=2,
                                                    shuffle=True, num_workers=2)
    else:
        
        transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ])
        # Load the CIFAR10 test dataset
        testset = torchvision.datasets.CIFAR10(root='../test/data', train=False,
                                            download=True, transform=transform)
        loader = torch.utils.data.DataLoader(testset, batch_size=32,
                                                shuffle=False, num_workers=2)
    
    return loader