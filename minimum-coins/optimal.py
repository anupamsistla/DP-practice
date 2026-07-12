class Solution:
    def MinimumCoins(self, coins, amount):
        prev = [0]*(amount+1)

        for a in range(amount + 1):
            if a % coins[0] == 0:
                prev[a] = a // coins[0]
            
            else:
                prev[a] = float("inf")
    
        for i in range(1, len(coins)):
            curr = [0]*(amount+1)
            for a in range(amount + 1):
                notTake = prev[a]
                take = float("inf")

                if a >= coins[i]:
                    take = 1 + curr[a - coins[i]]

                curr[a] = min(notTake, take)
            prev = curr
        return prev[amount]
            
# Time complexity: O(n * amount)
# Space complexity: O(n)
    
if __name__ == "__main__":
    dummy = Solution()
    print(dummy.MinimumCoins([1, 2, 5], 11))
    print(dummy.MinimumCoins([2, 5], 3))
    print(dummy.MinimumCoins([10], 5))
    print(dummy.MinimumCoins([1, 2, 3], 8))
    print(dummy.MinimumCoins([1, 2], 9))
    print(dummy.MinimumCoins([1, 3, 5], 7))