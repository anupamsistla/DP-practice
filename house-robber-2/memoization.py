class Solution:
    def foo(self, index, money, dp):
        if index == 0:
            return money[index]
        if index < 0:
            return 0
        if dp[index] != -1:
            return dp[index]
    
        pick = self.foo(index-2, money, dp) + money[index]
        notPick = self.foo(index-1, money, dp)
    
        dp[index] = max(pick, notPick)
        return dp[index]
    
    def houseRobber(self, money):
        n = len(money)
        temp1 = money[:n-1]
        temp2 = money[1:]
        dp1 = [-1]*(n-1)
        dp2 = [-1]*(n-1)

        return max(self.foo(n-2, temp1, dp1), self.foo(n-2, temp2, dp2))
    


if __name__ == "__main__":
    dummy = Solution()
    test1 = [2, 1, 4, 9, 10]

    print(dummy.houseRobber(test1))