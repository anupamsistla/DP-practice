from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        prev = [0] * m

        prev[0] = grid[0][0]

        for i in range(n):
            curr = [0] * m
            curr[0] = grid[0][0]
            for j in range(m):
                if i == 0 and j == 0:
                    continue

                up = grid[i][j] + prev[j] if i > 0 else float("inf")
                left = grid[i][j] + curr[j-1] if j > 0 else float('inf')
        
                curr[j] = min(up, left)     

            prev = curr          

        return prev[m-1]

if __name__ == "__main__":
    dummy = Solution()

    print(dummy.minPathSum([[5,9,6],[11,5,2]]))
    print(dummy.minPathSum([[1,2,3],[4,5,6]]))