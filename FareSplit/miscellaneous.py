def user_names():
    # Used to prompt the user for user names
    import numpy as np
    user = []
    while True:
        user = user + [input("Please input a user name: ")]
        print("Add another user?")
        another = input("Y/N: ")
        if another == "N":
            break
    user = np.array(user)
    return user

def initial_matrix(usernames):
    # Initialize the adjacency matrix
    # We use adjacency matrix instead of 
    # adjacency list since we expect that 
    # the graph would be dense at the beginning
    import numpy as np
    userNum = len(usernames)
    Adj_Matrix = np.zeros(shape = (userNum, userNum))
    return Adj_Matrix



def financial_activity():
    # Used to record one financial activity

    return 

