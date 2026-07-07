from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])        
        prev = [0]*n
        
        for i in range(m):
            curr = [0]*n
            for j in range(n):
                if i == 0 and j == 0:
                    curr[j] = grid[i][j]

                else:
                    up = grid[i][j]
                    left = grid[i][j]

                    up += prev[j] if i > 0 else float("inf")
                    left += curr[j-1] if j > 0 else float("inf")
                    curr[j] = min(up, left)
            prev = curr

        return curr[n-1]
    
# Time complexity: O(m*n)
# Space complexity: O(n)

if __name__ == "__main__":
    dummy = Solution()

    print(dummy.minPathSum([[5,9,6],[11,5,2]]))
    print(dummy.minPathSum([[1,2,3],[4,5,6]]))