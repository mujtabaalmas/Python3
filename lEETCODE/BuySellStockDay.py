##this is the logic for question 
#first loop through list best case iter the list first
#store ith (0 index) element in min_price because it the minimum price we first buy and then checks by iter i if there is any other minimum element(price) in the list than we select and update that price with i (the min price in which we buy stock) and than check maximum value (it is already initialze by 0) we add built in func max to find max num in the list and then when we find that maximum number greater than our minprice we minus it from max_profit and return it.

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        selectedList = iter(prices) 
        max_profit = 0
        min_price  = prices[0]
        for i in selectedList:
                if i < min_price:
                     min_price = i
                else:
                     max_profit = max(max_profit,i-min_price)
                     
        return max_profit
        
x = Solution()
print("Max Profit:",x.maxProfit([10,7,6,5,9]))