class Solution:
    def foo(self, i, j1, j2, g, dp):
        if j1 < 0 or j2 < 0 or j1 >= len(g[0]) or j2 >= len(g[0]):
            return float("-inf")

        if dp[i][j1][j2] != -1:
            return dp[i][j1][j2]

        if i == 0:
            if j1 != j2:
                return g[i][j1] + g[i][j2]

            else:
                return g[i][j1]


        dirs = [-1, 0, 1]

        maxSum = float("-inf")
        for x in dirs:
            for y in dirs:
                curr = g[i][j1] + g[i][j2] if j1 != j2 else g[i][j1]
                maxSum = max(maxSum, curr + self.foo(i-1, j1 + x, j2 + y, g, dp))

        dp[i][j1][j2] = maxSum
        return maxSum
        
    def aliceAndBob(self, n, m, g):
        prev = [[0] * m for _ in range(m)]

        for j1 in range(m):
            for j2 in range(m):
                if j1 != j2:
                    prev[j1][j2] = g[0][j1] + g[0][j2]
                else:
                    prev[j1][j2] = g[0][j1]

        for i in range(1, n):
            curr = [[0] * m for _ in range(m)]
            for j1 in range(m-1, -1, -1):
                for j2 in range(m-1, -1, -1):
                    dirs = [-1, 0, 1]
                    
                    maxSum = float("-inf")
                    for x in dirs:
                        for y in dirs:
                            currSum = g[i][j1] + g[i][j2] if j1 != j2 else g[i][j1]

                            if j1 + x in range(m) and j2 + y in range(m):
                                maxSum = max(maxSum, currSum + prev[j1 + x][j2 + y]) 
            
                    curr[j1][j2] = maxSum
            prev = curr

        return prev[0][m-1]

        # Your code goes here

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.aliceAndBob(3, 4, [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]))
    print(dummy.aliceAndBob(2, 3, [[4, 1, 2], [7, 3, 5]]))