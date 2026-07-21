class Solution:
    def foo(self, i, j, pat, str, dp):
        if i < 0 and j < 0:
            return True

        if i < 0 and j >= 0:
            return False
    
        if j < 0 and i >= 0:
            for ii in range(i+1):
                if pat[ii] != '*':
                    return False
            
            return True
        
        if dp[i][j] != -1:
            return dp[i][j]
    
        if pat[i] == str[j] or pat[i] == '?':
            dp[i][j] = self.foo(i-1, j-1, pat, str, dp)
            return dp[i][j]

        if pat[i] == '*':
            dp[i][j] = self.foo(i-1, j, pat, str, dp) or self.foo(i, j-1, pat, str, dp)
            return dp[i][j]
        
        dp[i][j] = False
        return dp[i][j]
    
    def wildCard(self, str: str, pat: str) -> bool:
        n, m = len(pat), len(str) 
        dp = [[-1]*m for _ in range(n)]
        return self.foo(n-1, m-1, pat, str, dp)
    
# Time complexity: O(n*m)
# Space complexity: O(n*m) + O(n+m) = O(n*m)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.wildCard("abdefcd", "ab*cd"))
    print(dummy.wildCard("xaylmz", "x?y*z"))
    print(dummy.wildCard("xyza", "x*z"))
    print(dummy.wildCard("abc", "a**bc"))
    print(dummy.wildCard("a", "****"))