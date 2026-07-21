class Solution:
    def foo(self, i, j, start, target):
        if i < 0:
            return j+1
        
        if j < 0:
            return i + 1
    
        if start[i] == target[j]:
            return self.foo(i-1, j-1, start, target)

        insert = 1 + self.foo(i, j-1, start, target)
        delete = 1 + self.foo(i-1, j, start, target)
        replace = 1 + self.foo(i-1, j-1, start, target)
        
        return min(insert, delete, replace)
        
    def editDistance(self, start, target):
        n, m = len(start), len(target)
        return self.foo(n-1, m-1, start, target)

# Time complexity: Exponential
# Space complexity: O(n+m)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.editDistance("horse", "ros"))
    print(dummy.editDistance("intention", "execution"))
    print(dummy.editDistance("abcdefg", "azced"))