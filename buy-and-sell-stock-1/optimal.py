class Solution:
    def stockBuySell(self, arr, n):
        minBuy = arr[0]
        maxProfit = 0

        for i in range(1, n):
            profit = arr[i] - minBuy
            maxProfit = max(maxProfit, profit)
            minBuy = min(minBuy, arr[i])
        return maxProfit


if __name__ == "__main__":
    dummy = Solution()
    print(dummy.stockBuySell([10, 7, 5, 8, 11, 9], 6))
    print(dummy.stockBuySell([5, 4, 3, 2, 1], 5))
    print(dummy.stockBuySell([3, 8, 1, 4, 6, 2], 6))