class Solution:
    def foo(self, index, heights, dp):
        if index == 0:
            return 0

        if dp[index] != -1:
            return dp[index]
        
        left = self.foo(index-1, heights, dp) + abs(heights[index-1] - heights[index])
        right = float("inf")

        if index >= 2:
            right = self.foo(index-2, heights, dp) + abs(heights[index-2] - heights[index])

        dp[index] = min(left, right)
        return dp[index]
    
    def frogJump(self, heights):
        dp = [-1]*len(heights)
        return self.foo(len(heights)-1, heights, dp)
    
if __name__ == "__main__":
    test1 = [10, 20, 30, 10]
    test2 = [30, 10, 60, 10, 60, 50]
    
    dummy = Solution()
    res1 = dummy.frogJump(test1)
    print(res1)