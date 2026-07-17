class Solution:
    # updated memoizaiton for tabulation
    def foo(self, n, m, str1, str2, dp):
        if n == 0 or m == 0:
            return 0
        
        if dp[n][m] != -1:
            return dp[n][m]
    
        if str1[n-1] == str2[m-1]:
            dp[n][m] = 1 + self.foo(n-1, m-1, str1, str2, dp)
            return dp[n][m]
        
        dp[n][m] = max(self.foo(n-1, m, str1, str2, dp), self.foo(n, m-1, str1, str2, dp))
        return dp[n][m]

    def lcs(self, str1, str2):
        n, m = len(str1), len(str2)
        dp = [[0]*(m+1) for _ in range(n+1)]

        for j in range(m+1):
            dp[0][j] = 0
        
        for i in range(n+1):
            dp[i][0] = 0

        for i in range(1, n+1):
            for j in range(1, m+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]

# Time complexity: O(m*n)
# Space complexity: O(m*n)
        
if __name__ == "__main__":
    dummy = Solution()
    print(dummy.lcs("bdefg", "bfg"))
    print(dummy.lcs("mnop", "mnq"))
    print(dummy.lcs("abc","dafb"))
    print(dummy.lcs("acd", "ced"))