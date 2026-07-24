class Solution:
    def foo(self, index, buy, fee, arr, n, dp):
        if index == n:
            return 0

        if dp[index][buy] != -1:
            return dp[index][buy]

        profit = 0

        if buy: 
            profit = max(-arr[index] + self.foo(index+1, 0, fee, arr, n, dp), self.foo(index + 1, 1, fee, arr, n, dp))

        else:
            profit = max(arr[index] + self.foo(index+1, 1, fee, arr, n, dp) - fee, self.foo(index+1, 0, fee, arr, n, dp))

        dp[index][buy] = profit
        return dp[index][buy]

    def stockBuySell(self, arr, n, fee):
        dp = [[-1]*2 for _ in range(n)]
        return self.foo(0, 1, fee, arr, n, dp)

# Time complexity: O(n*2)
# Space complexity: O(n) + O(n*2) = O(n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.stockBuySell([1, 3, 4, 0, 2], 5, 1))
    print(dummy.stockBuySell([1, 3, 2, 8, 4, 9], 6, 2))
    print(dummy.stockBuySell([10, 3, 7, 5, 1, 3], 6, 3))
