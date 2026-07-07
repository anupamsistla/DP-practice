from typing import List
class Solution:
    def foo(self, i, j, grid, dp):
        if i == 0 and j == 0:
            return grid[i][j]

        if i < 0 or j < 0:
            return float("inf")
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        up = grid[i][j] + self.foo(i-1, j, grid, dp)
        left = grid[i][j] + self.foo(i, j-1, grid, dp)
        
        dp[i][j] = min(up, left)
        return dp[i][j]
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])        
        dp = [[-1]*n for _ in range(m)]

        return self.foo(m-1, n-1, grid, dp)
    
# Time complexity: O(m*n)
# Space complexity: Path length = (m-1 + n-1) + (m*n) = O(m*n)

if __name__ == "__main__":
    dummy = Solution()

    print(dummy.minPathSum([[5,9,6],[11,5,2]]))
    print(dummy.minPathSum([[1,2,3],[4,5,6]]))