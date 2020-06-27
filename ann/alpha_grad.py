#especially used for large input values
#overcomes the overshoot of small errors


input, weight, goal_predi = (2, 0.5, 3)
ALPHA = 0.1

def grad_descent_alpha(alpha, weight, goal_predi, input):
    for i in range(20):
        pred = weight * input
        error = (pred - goal_predi) ** 2
        delt = (pred - goal_predi) * input
        weight = weight - (alpha * delt)
        print("Error: {}, Prediction: {} ".format(error, pred))

grad_descent_alpha(ALPHA, weight, goal_predi, input)
