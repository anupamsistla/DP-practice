class Solution:
    def foo(self, i, j, matrix):
        if i >= 0 and j >= 0 and matrix[i][j] == 1:
            return 0
        
        if i == 0 and j == 0:
            return 1

        if i < 0 or j < 0:
            return 0
        
        up = self.foo(i-1, j, matrix)
        left = self.foo(i, j-1, matrix)

        return up + left
    
    def uniquePathsWithObstacles(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        return self.foo(m-1, n-1, matrix)
    
# Time complexity: O(2^(m*n))
# Space complexity: Path length = O(m-1 + n-1) = O(m + n)

if __name__ == "__main__":
    dummy = Solution()

    print(dummy.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])) # return 2
    print(dummy.uniquePathsWithObstacles([[0, 0, 0], [0, 0, 0], [0, 0, 1]])) # return 0
    print(dummy.uniquePathsWithObstacles([[0, 0, 0], [0, 0, 1], [0, 1, 0]])) # return 0
    print(dummy.uniquePathsWithObstacles([[0, 0, 0, 0], [0, 0, 1, 0]])) # return 1

