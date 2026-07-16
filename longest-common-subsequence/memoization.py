class Solution:
    def foo(self, n, m, str1, str2, dp):
        if n < 0 or m < 0:
            return 0
        
        if dp[n][m] != -1:
            return dp[n][m]
        
        if str1[n] == str2[m]:
            return 1 + self.foo(n-1, m-1, str1, str2, dp)

        dp[n][m] = max(self.foo(n-1, m, str1, str2, dp), self.foo(n, m-1, str1, str2, dp))
        return dp[n][m]
    
    # AB | BE
    
    def lcs(self, str1, str2):
        n, m = len(str1), len(str2)
        dp = [[-1]*m for _ in range(n)]
        return self.foo(n-1, m-1, str1, str2, dp)
    
# Time complexity: O(m*n)
# Space complexity: O(m+n) 
        
if __name__ == "__main__":
    dummy = Solution()
    print(dummy.lcs("bdefg", "bfg"))
    print(dummy.lcs("mnop", "mnq"))
    print(dummy.lcs("abc","dafb"))
    print(dummy.lcs("acd", "ced"))