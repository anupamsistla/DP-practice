class Solution:
    def foo(self, index, amount, coins):
        if index == 0:
            if amount % coins[0] == 0:
                return amount // coins[0]
            else:
                return float("inf")
        
        notTake = self.foo(index-1, amount, coins)
        take = float("inf")

        if amount >= coins[index]:
            take = 1 + self.foo(index, amount - coins[index], coins)
        return min(notTake, take)
    
    def MinimumCoins(self, coins, amount):
        n = len(amount)
        return self.foo(n-1, amount, coins)

# Time complexity: O(2^amount/w)
# Space complexity: O(n + amount/w)
# Where w is the smallest denomination coin
    
if __name__ == "__main__":
    dummy = Solution()
    print(dummy.MinimumCoins([1, 2, 5], 11))
    print(dummy.MinimumCoins([2, 5], 3))
    print(dummy.MinimumCoins([10], 5))
    print(dummy.MinimumCoins([1, 2, 3], 8))
    print(dummy.MinimumCoins([1, 2], 9))