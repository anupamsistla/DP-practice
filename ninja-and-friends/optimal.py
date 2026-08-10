class Solution:    
    def aliceAndBob(self, n, m, g):
        ahead = [[0]*m for _ in range(m)]

        for j1 in range(m):
            for j2 in range(m):
                if j1 == j2:
                    ahead[j1][j2] = g[n-1][j1]
                else:
                    ahead[j1][j2] = g[n-1][j1] + g[n-1][j2]

        for i in range(n-2, -1, -1):
            curr = [[0]*m for _ in range(m)]
            for j1 in range(m-1, -1, -1):
                for j2 in range(m-1, -1, -1):
                    dirs = [-1, 0, 1]
                    maxSum = float("-inf")
            
                    for x in dirs:
                        for y in dirs:
                            currSum = g[i][j1] + g[i][j2] if j1 != j2 else g[i][j1]

                            if j1 + x in range(m) and j2 + y in range(m):
                                maxSum = max(maxSum, currSum + ahead[j1 + x][j2 + y])
            
                    curr[j1][j2] = maxSum

            ahead = curr

        return ahead[0][m-1]

# Time complexity: O(n * m^2)
# Space complexity: O(m^2) 

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.aliceAndBob(3, 4, [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]))
    print(dummy.aliceAndBob(2, 3, [[4, 1, 2], [7, 3, 5]]))