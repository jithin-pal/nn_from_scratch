import numpy as np

weights = np.array([0.1, 0.2, 0.3])
learning_rate = 0.01 #lr

def netowrk_prediction(inputs, weights):
    pred = inputs.dot(weights)  #weighted num of input and weights
    return pred
    
true_value = 2
toes = np.array([8.5, 9.5, 9.9, 9.0])
wlrec = np.array([0.65, 0.8, 0.8, 0.9])
nfans = np.array([1.2, 1.3, 0.5, 1.0])
input = np.array([toes[0],wlrec[0],nfans[0]])

pred = netowrk_prediction(input, weights+learning_rate)
error = (pred  - true_value) ** 2
print(error)