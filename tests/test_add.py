import unittest
import torch
import torch.nn as nn

def add(a, b):
    return a + b

class MyTestCase(unittest.TestCase):

    def test_add(self):
        result = add(2, 3)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()