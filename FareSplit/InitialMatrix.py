def gen_matrix():
    import userInput
    import matrixFun
    
    # First, we need to prompt the user for 
    # a list of user names
    user = userInput.user_names()
    
    # Initialize the adjacency matrix
    Adj_Matrix = matrixFun.initial_matrix(usernames = user)
    
    while True:
        print("Record a financial activity.")
        # Record a financial activity
        Fin_Act = userInput.financial_activity(usernames = user)
        
        # Update the Adjacency matrix
        Adj_Matrix = matrixFun.update_matrix(Adjacency_Matrix = Adj_Matrix, 
                                rowindex = Fin_Act[0],
                                colindex = Fin_Act[1],
                                debt_num = Fin_Act[2],
                                payprop = Fin_Act[3])
        print("Add another activity?")
        another = input("Y/N: ")
        if another == "N":
            break
    return user, Adj_Matrix



