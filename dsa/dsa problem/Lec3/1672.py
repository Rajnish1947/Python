# You are given a 2D integer array accounts, where each row represents a customer 
# and each column represents the amount of money the customer has in a particular bank.
#  Your task is to compute the wealth of the richest customer. A customer's wealth is defined 
# as the sum of the amounts they have across all their bank accounts.

# Example:

# accounts = [
#     [1, 2, 3],
#     [3, 2, 1]
# ]


# Customer 0 has wealth = 1 + 2 + 3 = 6

# Customer 1 has wealth = 3 + 2 + 1 = 6

# Both customers have the same wealth, so the output is 6.

def maxsum(accounts):
    ans=0
    for account in accounts:
        ans=max(ans,sum(account))
    return ans    
accounts=[[1,2,3],[1,3,5]]
print(maxsum(accounts))



