class Solution:
    def foo(self, index, heights, dp):
        if index == 0:
            return 0
        
        if dp[index] != -1:
            return dp[index]

        one = abs(heights[index-1] - heights[index]) + self.foo(index-1, heights, dp)
        
        two = float("inf")
        if index >= 2:
            two = abs(heights[index-2] - heights[index]) + self.foo(index-2, heights, dp)

        dp[index] = min(one, two)
        return dp[index]
        
    def frogJump(self, heights):
        n = len(heights)-1
        dp = [-1]*(n+1)

        return self.foo(n, heights, dp)

# Time complexity: O(n)
# Space complexity: O(n + n)
    
if __name__ == "__main__":
    dummy = Solution()
    
    print(dummy.frogJump([2, 1, 3, 5, 4]))
    print(dummy.frogJump([7, 5, 1, 2, 6]))

        