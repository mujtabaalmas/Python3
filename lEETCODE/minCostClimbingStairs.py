#minium cost for climbling stairs ------------
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
print("Minimmum cost:",xs.minCostClimbingStairs([15,10,20]))

