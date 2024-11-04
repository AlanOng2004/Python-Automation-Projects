import numpy as np

def sigmoid(x):
    # Activation Function: f(x) = 1 / (1 + e^(x))
    return 1 / (1 + np.exp(-x))

def mse_loss(y_true, y_pred): # calculates the mean squared error of the neural network
    # y_true and y_pred are numpy arrays of the same length.
    return((y_true - y_pred) ** 2).mean()

class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def feedfoward(self, inputs):
        # Weight inputs, add bias, then use the activation function
        total = np.dot(self.weights, inputs) + self.bias
        return (sigmoid(total))
    
class OurNeuralNetwork:
    '''
    A neural network with:
        - 2 inputs
        - a hidden layer with 2 neurons (h1, h2)
        - an output layer with 1 neuron (o1)
    Each neuron has the same weights and bias:
        - w = [0, 1]
        - b = 0
    '''

    def __init__(self):
        weights = np.array([0, 1])
        bias = 0

        self.h1 = Neuron(weights, bias)
        self.h2 = Neuron(weights, bias)
        self.o1 = Neuron(weights, bias)

    def feedfoward(self, x):
        output_h1 = self.h1.feedfoward(x)
        output_h2 = self.h2.feedfoward(x)

        # The inputs for o1 are the outputs for h1 and h2
        output_o1 = self.o1.feedfoward(np.array([output_h1, output_h2]))

        return output_o1

weights = np.array([0, 1])
bias = 4
n = Neuron(weights, bias)

network = OurNeuralNetwork()
x = np.array([2, 3])
print(n.feedfoward(x)) # prints h1, h2
print(network.feedfoward(x)) #prints o1

y_true = np.array([1, 0, 0, 1])
y_pred = np.array([0, 0, 0, 0])
print(mse_loss(y_true, y_pred))
