class Solution:
    def foo(self, index, heights, dp):
        if dp[index] != -1:
            return dp[index]
        
        if index == 0:
            return 0

        oneStep = abs(heights[index] - heights[index-1]) + self.foo(index-1, heights, dp)
        twoStep = float("inf")
        if index > 1:
            twoStep = abs(heights[index] - heights[index-2]) + self.foo(index-2, heights, dp)

        dp[index] = min(oneStep, twoStep)
        return dp[index]
    
    def frogJump(self, heights):
        n = len(heights) 

        prev2 = float("inf")
        prev1 = 0

        for index in range(1, n):
            oneStep = abs(heights[index] - heights[index-1]) + prev1
            twoStep = float("inf")
            if index > 1:
                twoStep = abs(heights[index] - heights[index-2]) + prev2

            prev2 = prev1
            prev1 = min(oneStep, twoStep)

        return prev1

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.frogJump([2, 1, 3, 5, 4]))
    print(dummy.frogJump([7, 5, 1, 2, 6]))
