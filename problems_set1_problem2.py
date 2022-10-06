"""
Justin Chen
Problem 2: Basic Operations
"""
import math

# 1. Plug two vairables into the compound interest formula and format the answer to two decimals
deposite_amounts = int(input('What is the deposite amounts?'))
interest_rate = float(input('What is the interest rate?')) / 100
total_wealth = deposite_amounts * pow((1 + (interest_rate)), 10)
print(f"Bill's total wealth is ${total_wealth:.2f}")

# 2. Double the deposite amount, move variables to solve the time t in compound interest formula
total_wealth = deposite_amounts * 2
time_needed = math.log(total_wealth, (1 + interest_rate))
print(f"It takes {time_needed:.2f} years to double Bill's money")

# 3. Modify the values of the variables, compare the total wealth and the desired amount
deposite_amounts = int(input('What is the deposite amounts?'))
interest_rate = float(input('What is the interest rate?')) / 100
total_wealth = deposite_amounts * pow((1 + (interest_rate)), 6)
print(total_wealth == (deposite_amounts * 2))

# 4. Created a list with names to be string value and money to be integer value
client_accounts = ["Bill", 1000, "Jack", 5000, "Amy", 6700, "Cindy", 5699, "Harry", 6700]
print(client_accounts)

# 5. Loop through the list and use every other value to be keys and values
Accounts = {client_accounts[i]: client_accounts[i + 1] for i in range(0, len(client_accounts), 2)}
print(Accounts)

# 6. Using the key as the first value of the tuple
# and value as the second value of the tuple
account_tuples = list(Accounts.items())
print(account_tuples)

# 7.
# List is a collection of ordered data
# Dictionary is a collection of unordered data that is represented in key-value pairs
# Sets are unordered collections of data