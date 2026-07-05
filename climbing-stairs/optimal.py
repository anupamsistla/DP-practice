class Solution:
    def climbStairs(self, n):
        dp = [-1] * (n+1)
        prev2, prev1 = 1, 1

        for i in range(2, n+1):
            dp[i] = prev1 + prev2
            prev2 = prev1
            prev1 = dp[i]
        return dp[n]

# Time complexity: O(n)
# Space complexity: O(1)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.climbStairs(2))
    print(dummy.climbStairs(3))
    print(dummy.climbStairs(4))
    