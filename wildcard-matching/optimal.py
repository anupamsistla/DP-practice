class Solution:
    def wildCard(self, str: str, pat: str) -> bool:
        n, m = len(pat), len(str) 
        prev = [False]*(m+1)
        prev[0] = True

        for j in range(1, m+1):
            prev[j] = False
        
        for i in range(1, n+1):
            curr = [False]*(m+1)
            flag = True
            for ii in range(1, i+1):
                if pat[ii-1] != '*':
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
    
# Time complexity: O(n*m)
# Space complexity: O(m)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.wildCard("abdefcd", "ab*cd"))
    print(dummy.wildCard("xaylmz", "x?y*z"))
    print(dummy.wildCard("xyza", "x*z"))
    print(dummy.wildCard("abc", "a**bc"))
    print(dummy.wildCard("a", "****"))