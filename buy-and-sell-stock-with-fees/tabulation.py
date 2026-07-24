class Solution:
    def stockBuySell(self, arr, n, fee):
        dp = [[0]*2 for _ in range(n+1)]

        for index in range(n-1, -1, -1):
            for buy in range(2):
                profit = 0
                
                if buy: 
                    profit = max(-arr[index] + dp[index+1][0], dp[index + 1][1])
        
                else:
                    profit = max(arr[index] + dp[index+1][1] - fee, dp[index+1][0])
        
                dp[index][buy] = profit

        return dp[0][1]

# Time complexity: O(n*2)
# Space complexity: O(n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.stockBuySell([1, 3, 4, 0, 2], 5, 1))
    print(dummy.stockBuySell([1, 3, 2, 8, 4, 9], 6, 2))
    print(dummy.stockBuySell([10, 3, 7, 5, 1, 3], 6, 3))
