class Solution:
    def foo(self, i, j1, j2, r, c, grid):
        if j1 < 0 or j1 >= c or j2 < 0 or j2 >= c:
            return float("-inf")

        if i == r-1:
            if j1 == j2:
                return grid[i][j1]
            
            else: 
                return grid[i][j1] + grid[i][j2]
        
        maxSum = float("-inf")
        delta = [-1, 0, 1]

        for d1 in delta:
            for d2 in delta:
                value = 0
                
                if j1 == j2:
                    value += grid[i][j1]
                
                else:
                    value += grid[i][j1] + grid[i][j2]

                value += self.foo(i+1, j1+d1, j2+d2, r, c, grid)
                maxSum = max(maxSum, value)
            
        return maxSum

    def aliceAndBob(self, r, c, grid):
        return self.foo(0, 0, c-1, r, c, grid)

# Time complexity: O(9^r)
# Space complexity: O(r)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.aliceAndBob(3, 4, [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]))
    print(dummy.aliceAndBob(2, 3, [[4, 1, 2], [7, 3, 5]]))
