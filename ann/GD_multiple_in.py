#gradient descent when we have multiple inputs
#perceptron

import numpy as np
import matplotlib.pyplot as plt

weights = [0.2, 0.5, -1]
inputs = [1,0.8,2]
goal_pred = [1] #won

def neural_network(inputs, weights, goal_pred):
    preds = np.dot(weights, inputs)
    error = (preds - goal_pred) ** 2
    delta = preds - goal_pred
    