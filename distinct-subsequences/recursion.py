class Solution:
    def foo(self, i, j, s, t):
        if j < 0:
            return 1
        
        if i < 0:
            return 0
    
        if s[i] == t[j]:
            return self.foo(i-1, j-1, s, t) + self.foo(i-1, j, s, t)
        
        return self.foo(i-1, j, s, t)

    def distinctSubsequences(self, s, t):
        n, m = len(s), len(t)
        return self.foo(n-1, m-1, s, t)
          
# Time complexity: O(2^(m+n))
# Space complexity: O(m+n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.distinctSubsequences("babgbag", "bag"))
    print(dummy.distinctSubsequences("axbxax", "axa"))
    print(dummy.distinctSubsequences("rabbbit", "rabbit"))