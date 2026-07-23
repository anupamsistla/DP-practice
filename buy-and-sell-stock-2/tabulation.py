class Solution:
    def stockBuySell(self, arr, n):
        dp = [[0]*2 for _ in range(n+1)]
        dp[n][0] = 0
        dp[n][1] = 0 

        for index in range(n-1, -1, -1):
            for buy in range(1, -1, -1):
                if buy:
                    profit = max(-arr[index] + dp[index + 1][0], dp[index + 1][1])
    
                else:
                    profit = max(arr[index] + dp[index + 1][1], dp[index+1][0])
        
                dp[index][buy] = profit

        return dp[0][1]

# Time complexity: O(n)
# Space complexity: O(n) 

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.stockBuySell([7, 1, 5, 3, 6, 4], 6))
    print(dummy.stockBuySell([9, 2, 6, 4, 7, 3], 6))
    print(dummy.stockBuySell([2, 3, 4, 5, 6], 5))
    print(dummy.stockBuySell([8, 6, 5, 4, 3], 5))