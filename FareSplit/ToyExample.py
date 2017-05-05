import numpy as np
import copy

userNum = 5
Adj_Matrix = np.zeros(shape = (userNum, userNum))

#########################
# A toy example
#########################
# Initialize the adjacency matrix
for i in range(userNum):
    for j in range(userNum):
        Adj_Matrix[i,j] = np.random.uniform(low = 0, high = 50, size = 1)

# Set the diagonal to 0
Adj_Matrix[range(userNum),range(userNum)] = 0
############################
#Prepare for Error Check



# The basic algorithm (can add more constraints later on)
# Eliminate all the cycles of length 2
Adj_Matrix = Adj_Matrix - Adj_Matrix.transpose()
Adj_Matrix[np.where(Adj_Matrix <= 0)] = 0

# Find all the structres of the form a -> b -> c and break them
# Method 1: Use graph theory
# Drawback: Requires Matrix multiplication
# Upside: Easy Math
while(True):
    Unweighted_Adj = copy.deepcopy(Adj_Matrix)
    Unweighted_Adj[np.where(Unweighted_Adj != 0)] = 1
    Unweighted_Adj_Square = np.matmul(Unweighted_Adj, Unweighted_Adj)
    Unweighted_Adj_Square[np.where(Unweighted_Adj_Square != 0)] = 1
    index = np.where((Unweighted_Adj_Square - Unweighted_Adj) == 1)
    if len(index[0]) == 0:
        break
    
    row_num = index[0][0]
    col_num = index[1][0]
    col_num1 = np.where(np.multiply(Unweighted_Adj[:,col_num], Unweighted_Adj[row_num,:]) != 0)[0][0]
    
    temp = min(Adj_Matrix[row_num, col_num1], Adj_Matrix[col_num1,col_num])
    Adj_Matrix[row_num, col_num] = Adj_Matrix[row_num, col_num] + temp
    if Adj_Matrix[col_num, row_num] != 0:
        temp1 = Adj_Matrix[row_num, col_num] - Adj_Matrix[col_num, row_num]
        if temp1 >= 0:
            Adj_Matrix[row_num, col_num] = temp1
            Adj_Matrix[col_num, row_num] = 0
        else:
            Adj_Matrix[row_num, col_num] = 0
            Adj_Matrix[col_num, row_num] = -temp1
    
    Adj_Matrix[row_num, col_num1] = Adj_Matrix[row_num, col_num1] - temp
    Adj_Matrix[col_num1,col_num] = Adj_Matrix[col_num1,col_num] - temp






