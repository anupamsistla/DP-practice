class Solution:
    def foo(self, index):
        if index == 0:
            return 1
        
        if index == 1:
            return 1
        
        return self.foo(index-1) + self.foo(index-2)
    
    def climbStairs(self, n):
        return self.foo(n)
    
# Time complexity: O(2^n)
# Space complexity: O(n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.climbStairs(2))
    print(dummy.climbStairs(3))

