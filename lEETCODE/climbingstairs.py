#climbling stairs how many ways o climb n no. of stairs -----  
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2  # f(1), f(2)
        for i in range(3, n + 1):
            a, b = b, a + b
        return b

x =Solution()
print(x.climbStairs(4))