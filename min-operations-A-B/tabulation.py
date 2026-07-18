class Solution:
    def minOperations(self, str1, str2):
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
        
        lcs = dp[n][m]
        leftDel = n - lcs
        rightAdd = m - lcs
        return leftDel + rightAdd

# Time complexity: O(m*n)
# Space complexity: O(m*n)
        
if __name__ == "__main__":
    dummy = Solution()
    print(dummy.minOperations("kitten", "sitting"))
    print(dummy.minOperations("flaw", "lawn"))
    print(dummy.minOperations("abcdef","ghijkl"))