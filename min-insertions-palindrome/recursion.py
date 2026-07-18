class Solution:
    def lcs(self, n, m, str1, str2):
        if n == 0 or m == 0:
            return 0
    
        if str1[n-1] == str2[m-1]:
            return 1 + self.lcs(n-1, m-1, str1, str2)
        
        return max(self.lcs(n-1, m, str1, str2), self.lcs(n, m-1, str1, str2))
    
    def minInsertion(self, s):
        n = m = len(s)
        return m - self.lcs(n, m, s, s[::-1])

# Time complexity: O(2^m+n)
# Space complexity: O(m+n) 
    
if __name__ == "__main__":
    dummy = Solution()
    print(dummy.minInsertion("abcaa"))
    print(dummy.minInsertion("codingninjas"))
    print(dummy.minInsertion("ba"))
