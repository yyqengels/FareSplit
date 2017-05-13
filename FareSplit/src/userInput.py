def user_names():
    # Used to prompt the user for user names
    import numpy as np
    user = []
    while True:
        temp = input("Please input a user name: ")
        while temp in user:
            print("You've already input this name, please alter it.")
            temp = input("Please input a user name: ")
        
        user = user + [temp]

        print("Add another user?")
        another = input("Y/N: ")
        if another == "N":
            break
    user = np.array(user)
    return user
###########################################


def financial_activity(usernames):
    # Used to find out who paid for the service?
    import numpy as np
    payer = []
    pay_num = []
    while True:
        temp = input("Please input a payer name: ")
        while temp not in usernames:
            print("The name you input is not one of the users.")
            temp = input("Please input a payer name: ")
        while temp in payer:
            print("You've already input this name, please alter it.")
            temp = input("Please input a payer name: ")

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
    row_index = np.zeros(shape = (1, len(payer)), dtype = 'int64')
    for i in range(len(payer)):
        row_index[0,i] = int(np.where(usernames == payer[i])[0][0])
    
    # Who used the service? And
    # who owes what to whom?
    # Multiple currencies#########!!!!!!
    #######
    # Allow adding new users on the fly
    payee = []
    debt = []
    print("Split the fare equally? ")
    go_dutch = input("Y/N: ")
    
    while True:
        temp = input("Please input a payee name: ")
        while temp not in usernames:
            print("The name you input is not one of the users.")
            temp = input("Please input a payee name: ")
        payee = payee + [temp]

        if go_dutch == "N":
            debt = debt + [float(input("How much should this person pay?"))]
        print("Add another payee?")
        another = input("Y/N? ")
        if another == "N":
            debt = np.array(debt)
            break
    
    payee = np.array(payee)
    
#==============================================================================
#     if sum(debt) != sum(paynum):
#         print("The sum of debt is not equal to the price of the service\n")
#         print("The sum of debt is " + str(sum(debt)) + "\n")
#         print("The price of the service is " + str(sum(paynum)) + "\n")
#         print("Do you want to proceed?\n")
#         print("If yes, we are going to assume that the price of the service is the sum of debt.\n")
#         print("If no, you will need to go back and change the debt.\n")
#         proceed = input("Y/N: ")
#==============================================================================
    
    # Can be resolved by user interface
    
    if go_dutch == "Y":
        debt = np.zeros(shape = len(payee))
        debt[:] = np.mean(pay_num)
    
    
    col_index = np.zeros(shape = (1, len(payee)), dtype = 'int64')
    for i in range(len(payee)):
        col_index[0,i] = int(np.where(usernames == payee[i])[0][0])
    
#==============================================================================
#     result["row_index"] = row_index
#     result["col_index"] = col_index
#     result["debt"] = debt
#     result["pay_prop"] = pay_prop
#==============================================================================
    return row_index, col_index, debt, pay_prop

###########################################




