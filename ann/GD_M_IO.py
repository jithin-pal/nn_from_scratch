#weight matrix
weights = [[0.1,0.5,0.3],
            [0.4,0.2,0.6],
            [1.0,0.25,-1]]


#input class values
toes = [8.5, 9.5,9.9,9.0]
wlrec =  [0.65,0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

#output class values
hurt = [0.1, 0.0, 0.0, 0.1]
win = [ 1, 1, 0, 1]
sad = [0.1, 0.0, 0.1, 0.2]

input = [toes[0], wlrec[0], nfans[0]]

#pred values
true =  [hurt[0], win[0], sad[0]]

error = [0,0,0]
delta = [0,0,0]

pred = neural_network(input, weights)

def neural_network(input, weights):
    #weighted sum of input and weights
    preds = weighted_sum(input, weights)
    return pred

def w_sum(inn, w_mat):
    for i in range(len(inn)):
         output += (inn[i] * w_mat[i])
    return output

def weighted_sum(inp, wei_matrix):
    output = [0,0,0]
    for i in range(len(inp)):
        output[i] = w_sum(inp, wei_matrix)

