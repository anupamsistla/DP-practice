class Solution:
    def foo(self, i, j, str1, str2, dp):
        if i == 0:
            return 0

        if j == 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if str1[i-1] == str2[j-1]:
            dp[i][j] = 1 + self.foo(i-1, j-1, str1, str2, dp)
            return dp[i][j]

        dp[i][j] = max(self.foo(i-1, j, str1, str2, dp), self.foo(i, j-1, str1, str2, dp))
        return dp[i][j]

    def lcs(self, str1, str2):
        m = len(str1)
        n = len(str2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 0

        return dp[m][n]

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.lcs("bdefg", "bfg"))
    print(dummy.lcs("mnop", "mnq"))
    print(dummy.lcs("abc","dafb"))
    print(dummy.lcs("acd", "ced"))