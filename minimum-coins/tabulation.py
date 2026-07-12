class Solution:
    def MinimumCoins(self, coins, amount):
        dp = [[0]*(amount+1) for _ in range(len(coins))]

        for a in range(amount + 1):
            if a % coins[0] == 0:
                dp[0][a] = a // coins[0]
            
            else:
                dp[0][a] = float("inf")
    
        for i in range(1, len(coins)):
            for a in range(amount + 1):
                notTake = dp[i-1][a]
                take = float("inf")

                if a >= coins[i]:
                    take = 1 + dp[i][a - coins[i]]

                dp[i][a] = min(notTake, take)
        return dp[len(coins)-1][amount]
            
# Time complexity: O(n * amount)
# Space complexity: O(n * amount)
    
if __name__ == "__main__":
    dummy = Solution()
    print(dummy.MinimumCoins([1, 2, 5], 11))
    print(dummy.MinimumCoins([2, 5], 3))
    print(dummy.MinimumCoins([10], 5))
    print(dummy.MinimumCoins([1, 2, 3], 8))
    print(dummy.MinimumCoins([1, 2], 9))
    print(dummy.MinimumCoins([1, 3, 5], 7))