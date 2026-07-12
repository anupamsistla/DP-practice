class Solution:
    def foo(self, index, amount, coins, dp):
        if dp[index][amount] != -1:
            return dp[index][amount]

        if index == 0:
            if amount % coins[0] == 0:
                return amount // coins[0]
            else:
                return float("inf")
        
        notTake = self.foo(index-1, amount, coins, dp)
        take = float("inf")

        if amount >= coins[index]:
            take = 1 + self.foo(index, amount - coins[index], coins, dp)

        dp[index][amount] = min(notTake, take)
        return dp[index][amount]
    
    def MinimumCoins(self, coins, amount):
        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(len(coins))]
        return self.foo(n-1, amount, coins, dp)
    
# Time complexity: O(n * amount)
# Space complexity: O(n * amount) + O(n + amount/w) = O(n * amount)
# Where w is the smallest denomination coin
    
if __name__ == "__main__":
    dummy = Solution()
    print(dummy.MinimumCoins([1, 2, 5], 11))
    print(dummy.MinimumCoins([2, 5], 3))
    print(dummy.MinimumCoins([10], 5))
    print(dummy.MinimumCoins([1, 2, 3], 8))
    print(dummy.MinimumCoins([1, 2], 9))
    print(dummy.MinimumCoins([1, 3, 5], 7))