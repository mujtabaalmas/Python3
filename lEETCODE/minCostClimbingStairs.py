#minium cost for climbling stairs ------------
# suppose we have cost i and ith index is the climbling cost of stairs we have to find the minimum cost first we take len of cost list then pass two check whether its length is equal to 0 or 1 and return 0 and 0th index respectively. then initialize our dp list we (we build another dp list where minimum cost id dp[i] ) we have initialize it with length of cost list and its 0th and 1st index with cost of 0 and first index repectively. then a for loop which starts from index 2 because we already initiazes value 0,1 and assign to dp array then for loop goes to n -1 iteration we apply algorithm ith -1 index and ith-2 index take minimum from it and add it to current cost and store it in dp array return the minimum of n-2 and n-1 from dp dp array that is the minimum cost.
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        print(cost)
        n = len(cost)
        if n == 0:
            return 0
        if n == 1:
            return cost[0]

        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[n-1], dp[n-2])

xs = Solution()
print("Minimmum cost:",xs.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
print('\n')
print("Minimmum cost:",xs.minCostClimbingStairs([10,15,20]))

