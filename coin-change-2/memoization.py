class Solution:
    def foo(self, index, amount, coins, dp):
        if dp[index][amount] != -1:
            return dp[index][amount]
        
        if index == 0:
            if amount % coins[0] == 0:
                return 1
            else:
                return 0

        notTake = self.foo(index-1, amount, coins, dp)
        take = 0

        if amount >= coins[index]:
            take = self.foo(index, amount - coins[index], coins, dp)
        
        dp[index][amount] = notTake + take
        return dp[index][amount]

    def count(self, coins, N, amount):
        dp = [[-1]*(amount+1) for _ in range(len(coins))]
        return self.foo(N-1, amount, coins, dp)
    
# Time complexity: O(n * amount) 
# Space complexity: O(n * amount) + O(amount/w) = O(n * amount)
# Where 'w' is the smallest denomination in coins

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.count([1,2,3], 3, 4))
    print(dummy.count([2,4,10], 3, 10))
    print(dummy.count([3,5,7,10], 4, 11))
    print(dummy.count([3,5,7], 3, 4))

       