class Solution:  
    def frogJump(self, heights):
        n = len(heights)-1
        dp = [-1]*(n+1)

        dp[0] = 0

        for i in range(1, n+1):
            one = abs(heights[i-1] - heights[i]) + dp[i-1]

            two = float("inf")
            if i >= 2:
                two = abs(heights[i-2] - heights[i]) + dp[i-2]
            
            dp[i] = min(one, two)

        return dp[n]

# Time complexity: O(n)
# Space complexity: O(n)
    
if __name__ == "__main__":
    dummy = Solution()
    
    print(dummy.frogJump([2, 1, 3, 5, 4]))
    print(dummy.frogJump([7, 5, 1, 2, 6]))

        