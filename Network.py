import numpy as np

class Network(object):
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.randn.randn(y, x)
                            for x, y in zip(sizes[:-1], sizes[1:])]

if __name__ == "__main__":
    n = Network([[2, 3, 1]])
    print ("layers:", n.num_layers)
    print ("sizes:", n.sizes)
    print ("biases:", n.biases)
    print ("weights:", n.weights)