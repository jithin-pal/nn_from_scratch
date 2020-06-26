# import numpy as np

# weights= 0.5
# input = 0.5
# goal_pred = 0.8
# lr = 0.001

# for i in range(1000):
#     prediction = input * weights
#     error = (prediction - goal_pred) ** 2

#     print("{} Prediction, {} error".format(prediction,error))

#     up_prediction = input * (weights + lr)
#     up_error = (goal_pred - up_prediction) ** 2

#     down_pred = input * (weights - lr)
#     down_error = (goal_pred - down_pred) ** 2

#     if(up_prediction > down_pred):
#         weights = weights - lr
    
#     if(down_pred > up_prediction):
#         weights = weights - lr

weight = 0.5
input = 0.5
goal_prediction = 0.8
step_amount = 0.001
for iteration in range(1101):
    prediction = input * weight
    error = (prediction - goal_prediction) ** 2
    print("Error:" + str(error) + " Prediction:" + str(prediction))

    up_prediction = input * (weight + step_amount)
    up_error = (goal_prediction - up_prediction) ** 2
    down_prediction = input * (weight - step_amount)
    down_error = (goal_prediction - down_prediction) ** 2
    if(down_error < up_error):
        weight = weight - step_amount

    if(down_error > up_error):
        weight = weight + step_amount