class Solution:
    def foo(self, n, m, str1, str2):
        if n < 0 or m < 0:
            return 0
    
        if str1[n] == str2[m]:
            return 1 + self.foo(n-1, m-1, str1, str2)
        
        return max(self.foo(n-1, m, str1, str2), self.foo(n, m-1, str1, str2))

    def minOperations(self, str1, str2):
        n, m = len(str1), len(str2)
        lcs = self.foo(n-1, m-1, str1, str2)
        leftDel = n - lcs
        rightAdd = m - lcs
        return leftDel + rightAdd
    
# Time complexity: O(2^(m+n))
# Space complexity: O(m+n) 
        
if __name__ == "__main__":
    dummy = Solution()
    print(dummy.minOperations("kitten", "sitting"))
    print(dummy.minOperations("flaw", "lawn"))
    print(dummy.minOperations("abcdef","ghijkl"))