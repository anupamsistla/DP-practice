class Solution:
    # updated memoization for tabulation
    def foo(self, i, j, start, target, dp):
        if i == 0:
            return j
        
        if j == 0:
            return i
        
        if dp[i][j] != -1:
            return dp[i][j]
    
        if start[i-1] == target[j-1]:
            dp[i][j] = self.foo(i-1, j-1, start, target, dp)
            return dp[i][j]

        insert = 1 + self.foo(i, j-1, start, target, dp)
        delete = 1 + self.foo(i-1, j, start, target, dp)
        replace = 1 + self.foo(i-1, j-1, start, target, dp)
        
        dp[i][j] = min(insert, delete, replace)
        return dp[i][j]
        
    def editDistance(self, start, target):
        n, m = len(start), len(target)
        dp = [[0]*(m+1) for _ in range(n+1)]
        
        for j in range(m+1):
            dp[0][j] = j
        
        for i in range(n+1):
            dp[i][0] = i

        for i in range(1, n+1):
            for j in range(1, m+1):
                if start[i-1] == target[j-1]:
                    dp[i][j] = dp[i-1][j-1]

                else:
                    insert = 1 + dp[i][j-1]
                    delete = 1 + dp[i-1][j]
                    replace = 1 + dp[i-1][j-1]

                    dp[i][j] = min(insert, delete, replace)
        
        return dp[n][m]
    
# Time complexity: O(n*m)
# Space complexity: O(n*m)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.editDistance("horse", "ros"))
    print(dummy.editDistance("intention", "execution"))
    print(dummy.editDistance("abcdefg", "azced"))