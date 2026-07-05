class Solution:
    def foo(self, money, dp):
        dp[0] = money[0]
        n = len(money)

        for i in range(1, n):
            inc = money[i] + dp[i-2] if i >= 2 else money[i]
            exc = dp[i-1]
            dp[i] = max(inc, exc)
        
        return dp[n-1]
        
    def houseRobber(self, money):
        n = len(money)

        money1 = money[:n-1]
        money2 = money[1:]

        dp1 = [-1]*(n-1)
        dp2 = [-1]*(n-1)

        return max(self.foo(money1, dp1), self.foo(money2, dp2))

# Time complexity: O(n)
# Space complexity: O(n + n + n + n)

if __name__ == "__main__":
    dummy = Solution()

    print(dummy.houseRobber([1, 2, 4]))
    print(dummy.houseRobber([2, 1, 4, 9]))
