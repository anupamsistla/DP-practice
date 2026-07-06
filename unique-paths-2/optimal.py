class Solution: 
    def uniquePathsWithObstacles(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        prev = [0]*n

        for i in range(m):
            curr = [0]*n
            for j in range(n):
                if i == 0 and j == 0:
                    curr[j] = 1
                
                elif i >= 0 and j >= 0 and matrix[i][j] == 1:
                    curr[j] = 0
                
                else:
                    up = prev[j] if i > 0 else 0
                    left = curr[j-1] if j > 0 else 0
                    curr[j] = up + left
            prev = curr
        
        return prev[n-1]

# Time complexity: O(m*n)
# Space complexity: O(n)

if __name__ == "__main__":
    dummy = Solution()

    print(dummy.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])) # return 2
    print(dummy.uniquePathsWithObstacles([[0, 0, 0], [0, 0, 0], [0, 0, 1]])) # return 0
    print(dummy.uniquePathsWithObstacles([[0, 0, 0], [0, 0, 1], [0, 1, 0]])) # return 0
    print(dummy.uniquePathsWithObstacles([[0, 0, 0, 0], [0, 0, 1, 0]])) # return 1