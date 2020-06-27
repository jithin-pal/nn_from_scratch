import numpy as np

weights= 0.5
input = 0.5
goal_pred = 0.8
lr = 0.001

for i in range(1000):
    prediction = input * weights
    error = (prediction - goal_pred) ** 2

    print("Error:" + str(error) + " Prediction:" + str(prediction))

    up_prediction = input * (weights + lr)
    up_error = (goal_pred - up_prediction) ** 2

    down_pred = input * (weights - lr)
    down_error = (goal_pred - down_pred) ** 2

    if(up_error > down_error):
        weights = weights - lr
    
    if(down_error > up_error):
        weights = weights + lr

