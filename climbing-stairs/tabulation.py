class Solution:
    def climbStairs(self, n):
        dp = [-1] * (n+1)
        dp[0], dp[1] = 1, 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# Time complexity: O(n)
# Space complexity: O(n)
if __name__ == "__main__":
    dummy = Solution()
    print(dummy.climbStairs(2))
    print(dummy.climbStairs(3))
    print(dummy.climbStairs(4))
    