class Solution:
    def foo(self, index, buy, arr, n, dp):
        if index == n:
            return 0

        profit = 0

        if buy:
            profit = max(-arr[index] + self.foo(index + 1, 0, arr, n, dp), self.foo(index + 1, 1, arr, n, dp))

        else:
            profit = max(arr[index] + self.foo(index + 1, 1, arr, n, dp), self.foo(index+1, 0, arr, n, dp))

        dp[index][buy] = profit
        return dp[index][buy]

    def stockBuySell(self, arr, n):
        dp = [[-1]*2 for _ in range(n)]
        return self.foo(0, 1, arr, n, dp)

# Time complexity: O(n)
# Space complexity: O(n) + O(n) = O(n) 

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.stockBuySell([7, 1, 5, 3, 6, 4], 6))
    print(dummy.stockBuySell([9, 2, 6, 4, 7, 3], 6))
    print(dummy.stockBuySell([2, 3, 4, 5, 6], 5))
    print(dummy.stockBuySell([8, 6, 5, 4, 3], 5))