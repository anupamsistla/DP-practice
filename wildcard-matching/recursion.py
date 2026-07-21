class Solution:
    def foo(self, i, j, pat, str):
        if i < 0 and j < 0:
            return True

        if i < 0 and j >= 0:
            return False
    
        if j < 0 and i >= 0:
            for ii in range(i+1):
                if pat[ii] != '*':
                    return False
            
            return True
    
        if pat[i] == str[j] or pat[i] == '?':
            return self.foo(i-1, j-1, pat, str)

        if pat[i] == '*':
            return self.foo(i-1, j, pat, str) or self.foo(i, j-1, pat, str)
        
        return False
    
    def wildCard(self, str: str, pat: str) -> bool:
        n, m = len(pat), len(str) 
        return self.foo(n-1, m-1, pat, str)
    
# Time complexity: Exponential
# Space complexity: O(n+m)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.wildCard("abdefcd", "ab*cd"))
    print(dummy.wildCard("xaylmz", "x?y*z"))
    print(dummy.wildCard("xyza", "x*z"))
    print(dummy.wildCard("abc", "a**bc"))
    print(dummy.wildCard("a", "****"))