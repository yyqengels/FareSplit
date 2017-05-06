def user_names():
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


def initial_matrix(user):
    import numpy as np
    userNum = len(user)
    Adj_Matrix = np.zeros(shape = (userNum, userNum)) 
    return Adj_Matrix



def financial_activity():
    return