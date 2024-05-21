'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 
'''

import time


'''
Approach 1:
1. For every element check if there is a future higher value.
2. Calculate profit.  Keep track of max_profit
O(n^2)
'''


print('Approach 1')

def max_profit(prices):
    mp = 0
    profit = 0
    for i in range(len(prices)):
        for j in range(i,len(prices)):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                if profit > mp:
                    mp = profit
    return mp


prices = [7,1,5,3,6,4]
#prices = [7,6,4,3,1]
#prices = [2,4,1]
start_time = time.time()
result = max_profit(prices)
end_time = time.time()
print(result)
print(end_time - start_time)

    
'''
Approach 2: 
1. Use two pointer. Pointer1 starts from 0. Pointer2 starts from 1
2. If prices[pointer1] <= prices[pointer2] record profit and move pointer2
3. If prices[pointer1] > prices[pointer2] move pointer1 to pointer2, move pointer2 one spot
O(n)

'''

print('approach 2')

def max_profit2(prices):
    pointer1 = 0
    pointer2 = 1
    mp = 0
    while pointer2 <= len(prices) - 1:
        if prices[pointer1] < prices[pointer2]:
            local_profit = prices[pointer2] - prices[pointer1]
            if local_profit > mp:
                mp = local_profit
            pointer2 += 1
        else:
            pointer1 = pointer2
            pointer2 += 1
    return mp
    

prices = [7,1,5,3,6,4]
#prices = [7,6,4,3,1]
#prices = [2,4,1]    # issue with three-element list
start_time = time.time()
result = max_profit2(prices)
end_time = time.time()
print(result)
print(end_time - start_time)
# Faster approach


'''
Extended problem: now you can buy and sell the stock more than once. Calculate the max profit
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
'''

print('Extended problem: day trading profit')

'''
Approach: 
1. Use two pointers. Pointer1 starts from 0. Pointer2 starts from 1
2. If prices[pointer1] <= prices[pointer2] record profit and move pointer2. Save profit
3. Use a new array from the element to the last element and run the process iteratively. 
4. If prices[pointer1] > prices[pointer2] move pointer1 to pointer2, move pointer2 one spot


'''

def day_trading_profit(prices):
    pointer1 = 0
    pointer2 = 1
    mp = 0
    profits = []
    total_profit = 0
    while pointer2 <= len(prices) - 1:
        if prices[pointer1] < prices[pointer2]:
            local_profit = prices[pointer2] - prices[pointer1]
            pointer1 += 1
            pointer2 += 1
            total_profit = total_profit + local_profit
        else:
            pointer1 = pointer2
            pointer2 += 1
    return total_profit


prices = [7,1,5,3,6,4]
result= day_trading_profit(prices)
print(result)