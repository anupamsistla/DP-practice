class Solution:
    def foo(self, i, j, s, t, dp):
        if dp[i][j] != -1:
            return dp[i][j]

        if j == 0:
            return 1

        if i == 0:
            return 0

        if s[i-1] == t[j-1]:
            dp[i][j] = self.foo(i-1, j-1, s, t, dp) + self.foo(i-1, j, s, t, dp)
            return dp[i][j]

        dp[i][j] = self.foo(i-1, j, s, t, dp)
        return dp[i][j]
        
    def distinctSubsequences(self, s, t):
        n = len(s)
        m = len(t)

        prev = [0]*(m+1)
        prev[0] = 1

        for i in range(1, n+1):
            curr = [0]*(m+1)
            prev[0] = 1
            for j in range(1, m+1):
                if s[i-1] == t[j-1]:
                    curr[j] = prev[j-1] + prev[j]
                
                else:
                    curr[j] = prev[j]   
            prev = curr

        return prev[m]
        

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.distinctSubsequences("babgbag", "bag"))
    print(dummy.distinctSubsequences("axbxax", "axa"))
    print(dummy.distinctSubsequences("rabbbit", "rabbit"))