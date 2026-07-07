from typing import List
class Solution:
    def foo(self, i, j, grid):
        if i == 0 and j == 0:
            return grid[i][j]

        if i < 0 or j < 0:
            return float("inf")
        
        up = grid[i][j] + self.foo(i-1, j, grid)
        left = grid[i][j] + self.foo(i, j-1, grid)
        return min(up, left)
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        return self.foo(m-1, n-1, grid)
    
# Time complexity: O(2^(m*n))
# Space complexity: Path length = O(m-1 + n-1) = O(m+n)

if __name__ == "__main__":
    dummy = Solution()

    print(dummy.minPathSum([[5,9,6],[11,5,2]]))
    print(dummy.minPathSum([[1,2,3],[4,5,6]]))