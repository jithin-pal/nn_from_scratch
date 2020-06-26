import numpy as np

weights= 0.5
input = 0.5
goal_pred = 0.8
lr = 0.001

def Gradient_descent(input, weights, lr, goal_pred):
    for i in range(20):
        prediction = input * weights
        error = (prediction - goal_pred) ** 2
        #compute both amount and prediction of error and weights
        direction_and_weight_value = (prediction - goal_pred) * input
        weights = weights - direction_and_weight_value
        print("ERROR {}, PREDICTION {}".format(error, prediction))
    

Gradient_descent(input, weights, lr, goal_pred)
