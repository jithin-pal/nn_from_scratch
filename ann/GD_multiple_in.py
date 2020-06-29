#gradient descent when we have multiple inputs
#perceptron - mul inp to single output arch

import numpy as np
import matplotlib.pyplot as plt

weights = [0.2, 0.5, -1]
inputs = [3,0.8,4]
goal_pred = 1 #won
alpha = 0.01

def neural_network(inputs, weights):
    output = 0
    for i in range(len(inputs)):
        output += (inputs[i] * weights[i]) #weighted sum of all weights and inputs
    return output

# pred  =neural_network(inputs, weights)
# error = (pred - goal_pred) ** 2
# delta = pred - goal_pred

def weight_delta_calu(delta, inputs):
    output = [0,0,0]
    for i in range(len(output)):
        output[i] = delta[i] * inputs
    return output

for i in range(3):
    pred  = neural_network(inputs, weights)
    error = (pred - goal_pred) ** 2
    delta = pred - goal_pred
    # weight_delta = weight_delta_calu(delta, inputs)
    print("iteration: {},  Prediction: {}, Error: {}, Weight Delta: {}".format(i, pred, error))
    # for j in range(len(weights)):
    #     weights[j] -= alpha * weight_delta[i]
    #     print("Weights: {}".format(weights[j]))








