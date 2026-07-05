class Solution:
    def foo(self, money, dp):
        dp[0] = money[0]
        n = len(money)

        for i in range(1, n):
            pick = dp[i-2] + money[i] if i >= 2 else money[i]
            notPick = dp[i-1]

            dp[i] = max(pick, notPick)
        
        return dp[-1]
        
    def houseRobber(self, money):
        n = len(money)
        temp1 = money[:n-1]
        temp2 = money[1:]
        dp1 = [-1]*(n-1)
        dp2 = [-1]*(n-1)

        return max(self.foo(temp1, dp1), self.foo(temp2, dp2))
    


if __name__ == "__main__":
    dummy = Solution()
    test1 = [2, 1, 4, 9, 10]

    print(dummy.houseRobber(test1))