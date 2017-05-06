# This function will prompt the user for user input
# and initialize the adjacency matrix
import numpy as np
# First, we need to prompt the user for 
# a list of user names
user = []
while True:
    user = user + [input("Please input a user name: ")]
    print("Add another user?")
    another = input("Y/N: ")
    if another == "N":
        break

user = np.array(user)
##
# Can check if there are duplicated names

# Initialize the adjacency matrix
userNum = len(user)
Adj_Matrix = np.zeros(shape = (userNum, userNum)) 

########
# Secondly, we need to prompt the user for 
# financial activities


# Who paid for the service?
payer = []
pay_num = []
while True:
    payer = payer + [input("Please input a payer name: ")]
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


# Who enjoied the service? And
# Who owes what to whom?
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
    print("The sum of debt is " + sum(debt) + "\n")
    print("The price of the service is " + sum(pay_num) + "\n")
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


# Update the Adjacency matrix
for i in row_index:
    for j in col_index:
        if i == j:
            continue
        Adj_Matrix[i, j] = debt[j] * pay_prop[i]


# Some more users?




####
#np.append(Adj_Matrix , , axix = 1)
  
