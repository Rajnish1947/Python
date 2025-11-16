# buy and shell

def stock (prices):
    n=len(prices)

    max_profit=0
    min_buy = float('inf')
    for i in range(0,n):
        min_buy=min(min_buy,prices[i])
        max_profit=max(max_profit,(prices[i]-min_buy))
              
    return max_profit
prices = [7, 1, 5, 3, 6, 4]
print(stock(prices))         


# def stock (prices):
#     n=len(prices)
#     maxprofit=0
#     for i in range(0,n):
#         for j in range(i+1,n):
#             if prices[j]>prices[i]:
#                 prpfot=prices[j]-prices[i]
#                 maxprofit=max(maxprofit,prpfot)
#     return maxprofit
# prices = [7,1,5,3,6,4]
# print(stock(prices))            

