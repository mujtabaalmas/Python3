from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        res = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                total = 0
                count = 0
                # Traverse the 3x3 neighborhood
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        
                        ni, nj = i + dx, j + dy
                        # Check if neighbor is in bounds
                        if 0 <= ni < m and 0 <= nj < n:
                            
                            total += img[ni][nj]
                            count += 1
                res[i][j] = total // count  # Floor divisionn
        return res

sol = Solution()
img = [
    [100, 200, 100],
    [200,  50, 200],
    [100, 200, 100]
]

print(f"\nOriginal image: {img}\nSolved image: ",sol.imageSmoother(img))

#print(sol.imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))