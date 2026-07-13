class Solution:
    def count(self, coins, N, amount):
        dp = [[0]*(amount + 1) for _ in range(len(coins))]

        for a in range(amount + 1):
            if a % coins[0] == 0:
                dp[0][a] = 1
        
        for i in range(1, len(coins)):
            for a in range(amount + 1):
                notTake = dp[i-1][a]
                take = 0

                if a >= coins[i]:
                    take = dp[i][a - coins[i]]
        
                dp[i][a] = notTake + take

        return dp[N-1][amount]
    
# Time complexity: O(n * amount) 
# Space complexity: O(n * amount)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.count([1,2,3], 3, 4))
    print(dummy.count([2,4,10], 3, 10))
    print(dummy.count([3,5,7,10], 4, 11))
    print(dummy.count([3,5,7], 3, 4))
