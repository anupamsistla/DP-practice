class Solution:
    def foo(self, i, j, str, pat, dp):
        if i == 0 and j == 0:
            return True

        if i >= 1 and j == 0:
            for ii in range(i):
                if pat[ii] != "*":
                    return False

            return True

        if j >= 1 and i == 0:
            return False

        if dp[i][j] != -1:
            return dp[i][j]

        if pat[i-1] == str[j-1] or pat[i-1] == "?":
            dp[i][j] = self.foo(i-1, j-1, str, pat, dp)
            return dp[i][j]

        if pat[i-1] == "*":
            dp[i][j] = self.foo(i-1, j, str, pat, dp) or self.foo(i, j-1, str, pat, dp)
            return dp[i][j]

        dp[i][j] = False
        return dp[i][j]
        

    def wildCard(self, str: str, pat: str) -> bool:
        n = len(pat)
        m = len(str)

        prev = [False] * (m+1)

        prev[0] = True

        for j in range(1, m+1):
            prev[j] = False


        for i in range(1, n+1):
            curr = [0] * (m+1)
            flag = True
            for ii in range(i):
                if pat[ii] != '*':
                    flag = False

            curr[0] = flag
            for j in range(1, m+1):
                if pat[i-1] == str[j-1] or pat[i-1] == '?':
                    curr[j] = prev[j-1]
                
        
                elif pat[i-1] == '*':
                    curr[j] = prev[j] or curr[j-1]
                
                else:
                    curr[j] = False

            prev = curr

        return prev[m]
                



if __name__ == "__main__":
    dummy = Solution()
    print(dummy.wildCard("abdefcd", "ab*cd"))
    print(dummy.wildCard("xaylmz", "x?y*z"))
    print(dummy.wildCard("xyza", "x*z"))
    print(dummy.wildCard("abc", "a**bc"))
    print(dummy.wildCard("", "****"))