def user_names():
    # Used to prompt the user for user names
    import numpy as np
    user = []
    while True:
        temp = input("Please input a user name: ")
        while temp in user:
            print("You've already input this name, please alter it.")
            temp = input("Please input a user name: ")
        
        del temp
        user = user + [temp]
        print("Add another user?")
        another = input("Y/N: ")
        if another == "N":
            break
    user = np.array(user)
    return user
###########################################
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

def payer_names(user):
    import numpy as np
    # Who paid for the service?
    payer = []
    pay_num = []
    while True:
        temp = input("Please input a payer name: ")
        while temp not in user:
            print("The name you input is not one of the users.")
            temp = input("Please input a payer name: ")
        while temp in payer:
            print("You've already input this name, please alter it.")
            temp = input("Please input a payer name: ")
        del temp
        payer = payer + [temp]
        pay_num = pay_num + [float(input("How much did this person pay? "))]
        print("Add another payer?")
        another = input("Y/N? ")
        if another == "N":
            break
    payer = np.array(payer)
    pay_num = np.array(pay_num)
    pay_prop = pay_num / sum(pay_num)
    # Check all elements of payer are in user
    # User interface can probably resolve this issue
    row_index = np.zeros(shape = (1, len(payer)))
    for i in range(len(payer)):
        row_index[0,i] = np.where(user == payer[i])[0][0]
    
    return payer, pay_num, pay_prop, row_index
###########################################

def payee_names(pay_num):
    # Who enjoied the service? And
    # Who owes what to whom?
    import numpy as np
    payee = []
    debt = []
    print("Split the fare equally? ")
    go_dutch = input("Y/N: ")
    
    while True:
        payee = payee + [input("Please input a payee name: ")]
        if go_dutch == "N":
            debt = debt + [float(input("How much should this person pay?"))]
        print("Add another payee?")
        another = input("Y/N? ")
        if another == "N":
            debt = np.array(debt)
            break
    
    payee = np.array(payee)
    
    if sum(debt) != sum(pay_num):
        print("The sum of debt is not equal to the price of the service\n")
        print("The sum of debt is " + str(sum(debt)) + "\n")
        print("The price of the service is " + str(sum(pay_num)) + "\n")
        print("Do you want to proceed?\n")
        print("If yes, we are going to assume that the price of the service is the sum of debt.\n")
        print("If no, you will need to go back and change the debt.\n")
        proceed = input("Y/N: ")
    
    # Can be resolved by user interface
    
    if go_dutch == "Y":
        debt = np.zeros(shape = len(payee))
        debt[:] = np.mean(pay_num)
    
    
    col_index = np.zeros(shape = (1, len(payee)))
    for i in range(len(payee)):
        col_index[0,i] = np.where(user == payee[i])[0][0]
    
    return debt, col_index

###########################################

def update_matrix(Adjacency_Matrix, rowindex, colindex, debt_num, payprop):
    # Update the Adjacency matrix
    for i in rowindex:
        for j in colindex:
            if i == j:
                continue
            Adjacency_Matrix[i, j] = Adjacency_Matrix[i, j] + debt_num[j] * payprop[i]
    return Adjacency_Matrix


