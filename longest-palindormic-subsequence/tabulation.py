class Solution:
    def longestPalinSubseq(self, s):
        n = m = len(s)
        dp = [[0]*(m+1) for _ in range(n+1)]

        for j in range(m+1):
            dp[0][j] = 0
        
        for i in range(n+1):
            dp[i][0] = 0

        str1 = s
        str2 = s[::-1]

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
    print(dummy.longestPalinSubseq("baax"))
    print(dummy.longestPalinSubseq("eeeme"))
    print(dummy.longestPalinSubseq("bbabcbcab"))