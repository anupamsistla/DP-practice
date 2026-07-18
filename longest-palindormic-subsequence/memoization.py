class Solution:
    def lcs(self, n, m, str1, str2, dp):
        if dp[n][m] != -1:
            return dp[n][m]
        
        if n == 0 or m == 0:
            return 0
    
        if str1[n-1] == str2[m-1]:
            dp[n][m] = 1 + self.lcs(n-1, m-1, str1, str2, dp)
            return dp[n][m]
        
        dp[n][m] = max(self.lcs(n-1, m, str1, str2, dp), self.lcs(n, m-1, str1, str2, dp))
        return dp[n][m]
    
    def longestPalinSubseq(self, s):
        n = m = len(s)
        dp = [[-1]*(m+1) for _ in range(n+1)]
        return self.lcs(n, m, s, s[::-1], dp)
    
# Time complexity: O(m*n)
# Space complexity: O(m*n) + O(m+n) = O(m*n)
    
if __name__ == "__main__":
    dummy = Solution()
    print(dummy.longestPalinSubseq("baax"))
    print(dummy.longestPalinSubseq("eeeme"))
    print(dummy.longestPalinSubseq("bbabcbcab"))