class Solution:
    def maxProfit(self, prices):
        dp = [[0]*2 for _ in range(len(prices)+2)]
        n = len(prices)

        for index in range(n-1, -1, -1):
            for buy in range(2):
                profit = 0
        
                if buy:
                    profit = max(-prices[index] + dp[index+1][0], dp[index+1][1])
        
                else:
                    profit = max(prices[index] + dp[index+2][1], dp[index+1][0])
        
                dp[index][buy] = profit 

        return dp[0][1]

# Time complexity: O(n*2)
# Space complexity: O(n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.maxProfit([1,2,3,0,2]))
    print(dummy.maxProfit([1]))
    print(dummy.maxProfit([3,2,6,5,0,3]))
