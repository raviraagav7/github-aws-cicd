import unittest
import torch
import torch.nn as nn

class MyTestCase(unittest.TestCase):
    def test_relu(self):
        relu = nn.ReLU()
        input = torch.tensor([-1, 0, 1])
        expected_output = torch.tensor([0, 0, 1])
        output = relu(input)
        self.assertTrue(torch.all(torch.eq(output, expected_output)))

    def test_conv2d(self):
        conv = nn.Conv2d(3, 64, 3)
        input = torch.randn(1, 3, 32, 32)
        output = conv(input)
        self.assertEqual(output.size(), torch.Size([1, 64, 30, 30]))

if __name__ == '__main__':
    unittest.main()