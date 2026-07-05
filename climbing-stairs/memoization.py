class Solution:
    def foo(self, index, dp):
        if index == 0:
            return 1
        
        if index == 1:
            return 1
        
        if dp[index] != -1:
            return dp[index]
        
        
        dp[index] = self.foo(index-1, dp) + self.foo(index-2, dp)
        return dp[index]
    
    def climbStairs(self, n):
        dp = [-1] * (n+1)
        return self.foo(n, dp)

# Time complexity: O(n)
# Space complexity: O(n + n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.climbStairs(2))
    print(dummy.climbStairs(3))
    print(dummy.climbStairs(4))
    
