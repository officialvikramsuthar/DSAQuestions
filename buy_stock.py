# prices = [7,1,5,3,6,4]
# prices = [2,4,1]
# prices = [2,1,2,0,1,2]
# prices = []
# get two points min and max
# loop through arr
# check if current el is greater than max
index = 0 
max_profit = 0 

for i in range(1, len(prices)):
    temp_profit = prices[i] - prices[index] 
    max_profit = max(max_profit, temp_profit)
    if prices[i] < prices[index]:
        index = i

print(max_profit)