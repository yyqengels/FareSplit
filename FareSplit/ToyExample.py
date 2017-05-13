import numpy as np
import copy
import InitialMatrix
Adj_Matrix = InitialMatrix.gen_matrix()
#########################
# A toy example
#########################

##################
userNum = 30
Adj_Matrix = np.zeros(shape = (userNum, userNum))


# Initialize the adjacency matrix
for i in range(userNum):
    for j in range(userNum):
        Adj_Matrix[i,j] = np.random.uniform(low = 0, high = 50, size = 1)

# Set the diagonal to 0
Adj_Matrix[range(userNum),range(userNum)] = 0
############################
## Prepare for Error Check
# Everyone's net amoount
Net_Amount = np.zeros(shape = (1, userNum))
for i in range(userNum):
    Net_Amount[0,i] = np.sum(Adj_Matrix[:,i]) - np.sum(Adj_Matrix[i,:])

# Check if the matrix is generated correctly
np.sum(Net_Amount)


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
        del temp1
    
    Adj_Matrix[row_num, col_num1] = Adj_Matrix[row_num, col_num1] - temp
    Adj_Matrix[col_num1,col_num] = Adj_Matrix[col_num1,col_num] - temp
    del temp
###################################
## Error Check
# Check 1: 
# Everyone's net amount should remain the same after the algorithm
Net_Amount_Check = np.zeros(shape = (1, userNum))
for i in range(userNum):
    Net_Amount_Check[0,i] = np.sum(Adj_Matrix[:,i]) - np.sum(Adj_Matrix[i,:])

tolerance = 1e-5
check1 = Net_Amount_Check - Net_Amount
check1[np.where(abs(check1) <= tolerance)] = 0
if np.count_nonzero(check1) == 0:
    print("Pass Check 1")

# Check 2:
# The total net amount should be 0
check2 = np.sum(Net_Amount_Check)
if abs(check2) <= tolerance:
    check2 = 0
if check2 == 0:
    print("Pass Check 2")

###################################
# Result output
# We can print out a list containing the information of who owes what to whom
# Or we can use the package (hopefully) igraph to print out a directed graph
# to illustrate the result
########
# Method 1: List
user = range(userNum)

for i in range(userNum):
    for j in range(userNum):
        if Adj_Matrix[i,j] == 0:
            continue
        print("User " + str(user[i]) + " owes " + str(user[j]) + " "+str(Adj_Matrix[i, j]) + " dollars.")
        
# Method 2: Directed graph (coming up)


