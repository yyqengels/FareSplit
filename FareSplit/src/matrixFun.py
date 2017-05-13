def initial_matrix(usernames):
    # Initialize the adjacency matrix
    # We use adjacency matrix instead of 
    # adjacency list since we expect that 
    # the graph would be dense at the beginning
    import numpy as np
    userNum = len(usernames)
    Adj_Matrix = np.zeros(shape = (userNum, userNum))
    return Adj_Matrix
###########################################

def update_matrix(Adjacency_Matrix, rowindex, colindex, debt_num, payprop):
    import numpy as np
    # Update the Adjacency matrix
    for i in range(rowindex.size):
        for j in range(colindex.size):
            row = int(np.ndarray.tolist(rowindex)[0][i])
            col = int(np.ndarray.tolist(colindex)[0][j])
            if row == col:
                continue
            Adjacency_Matrix[row, col] += debt_num[j] * payprop[i]
    return Adjacency_Matrix

