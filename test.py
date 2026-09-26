class Solution:
    def foo(self, i, coins, amount, dp):
        if dp[i][amount] != -1:
            return dp[i][amount]

        if i == 0:
            if amount % coins[0] == 0:
                return amount // coins[0]
            else:
                return 0

        notTake = self.foo(i-1, coins, amount, dp)

        take = float("inf")

        if coins[i] <= amount:
            take = 1 + self.foo(i, coins, amount - coins[i], dp)

        dp[i][amount] = min(notTake, take)
        return dp[i][amount]

    
    def MinimumCoins(self, coins, amount):
        n = len(coins)
        prev = [0] * (amount + 1)

        for a in range(amount+1):
            if a % coins[0] == 0:
                prev[a] = a // coins[0]


        for i in range(1, n):
            curr = [0] * (amount + 1)
            for amount in range(0, amount+1):
                notTake = prev[amount]
                
                take = float("inf")
        
                if coins[i] <= amount:
                    take = 1 + curr[amount - coins[i]]
        
                curr[amount] = min(notTake, take)
            prev = curr

        return prev[amount]


if __name__ == "__main__":
    dummy = Solution()
    print(dummy.MinimumCoins([1, 2, 5], 11))
    print(dummy.MinimumCoins([2, 5], 3))
    print(dummy.MinimumCoins([10], 5))
    print(dummy.MinimumCoins([1, 2, 3], 8))
    print(dummy.MinimumCoins([1, 2], 9))
    print(dummy.MinimumCoins([1, 3, 5], 7))