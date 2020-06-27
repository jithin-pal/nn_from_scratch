import numpy as np
import matplotlib.pyplot as plt

weight , goal_pred, input = (0.0, 0.8, 2)

lr = 0.001

def Gradient_descent(input, weights, lr, goal_pred):
    for i in range(20):
        prediction = input * weights
        error = (prediction - goal_pred) ** 2
        #compute both amount and prediction of error and weights
        direction_and_weight_value = (prediction - goal_pred) * input
        weights = weights - direction_and_weight_value
        print("ERROR {}, PREDICTION {}".format(error, prediction))
    
# Gradient_descent(input, weight, lr, goal_pred)

def Gradient_descent_action(input, weight, goal_pred):
    er = []
    de = []
    for i in range(50):
        print("weight: {}".format(weight))
        pred = input * weight
        error = (pred - goal_pred) ** 2
        er.append(error)
        delta = pred - goal_pred
        de.append(delta)
        weight_delta = delta * input
        weight = weight - weight_delta
        print("Error: {} Prediction {}".format(error,pred))
        print("Delta: {} Weight Delta {}".format(delta, weight_delta))
    plt.plot(de)
    plt.show()
    return delta, weight_delta,error,pred

delta, weight_delta, error, pred = Gradient_descent_action(input, weight, goal_pred)
