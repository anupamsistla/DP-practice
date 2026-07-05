class Solution:
    def foo(self, index, money, dp):
        if index < 0:
            return 0
        
        if dp[index] != -1:
            return dp[index]

        inc = money[index] + self.foo(index-2, money, dp)
        exc = self.foo(index-1, money, dp)
        
        dp[index] = max(inc, exc)
        return dp[index]
        
    def houseRobber(self, money):
        n = len(money)

        money1 = money[:n-1]
        money2 = money[1:]

        dp1 = [-1]*(n-1)
        dp2 = [-1]*(n-1)

        return max(self.foo(n-2, money1, dp1), self.foo(n-2, money2, dp2))

# Time complexity: O(n)
# Space complexity: O(n + n + n + n + n)

if __name__ == "__main__":
    dummy = Solution()

    print(dummy.houseRobber([1, 2, 4]))
    print(dummy.houseRobber([2, 1, 4, 9]))
