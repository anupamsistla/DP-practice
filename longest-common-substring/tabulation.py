class Solution:
    def lcs(self, str1, str2):
        n, m = len(str1), len(str2)
        dp = [[0]*(m+1) for _ in range(n+1)]

        for j in range(m+1):
            dp[0][j] = 0
        
        for i in range(n+1):
            dp[i][0] = 0

        toRet = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    toRet = max(toRet, dp[i][j])
                else:
                    dp[i][j] = 0
        return toRet

# Time complexity: O(m*n)
# Space complexity: O(m*n)
        
if __name__ == "__main__":
    dummy = Solution()
    print(dummy.lcs("bdefg", "bfg"))
    print(dummy.lcs("mnop", "mnq"))
    print(dummy.lcs("abc","dafb"))
    print(dummy.lcs("acd", "ced"))