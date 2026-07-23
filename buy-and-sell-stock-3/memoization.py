class Solution:
    def foo(self, index, buy, cap, arr, n, dp):
        if index == n:
            return 0

        if cap == 0:
            return 0

        if dp[index][buy][cap] != -1:
            return dp[index][buy][cap]

        profit = 0

        if buy:
            profit = max(-arr[index] + self.foo(index+1, 0, cap, arr, n, dp), self.foo(index+1, 1, cap, arr, n, dp))

        else:
            profit = max(arr[index] + self.foo(index+1, 1, cap-1, arr, n, dp), self.foo(index+1, 0, cap, arr, n, dp))

        dp[index][buy][cap] = profit
        return dp[index][buy][cap]
        
    def stockBuySell(self, arr, n):
        dp = [[[-1]*3 for _ in range(2)] for _ in range(n)]
        return self.foo(0, 1, 2, arr, n, dp)

# Time complexity: O(n*2*3) = O(n)
# Space complexity: O(n*2*3) + O(n) = O(n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.stockBuySell([4, 2, 7, 1, 11, 5], 6))
    print(dummy.stockBuySell([1, 3, 2, 8, 4, 9], 6))
    print(dummy.stockBuySell([5, 7, 2, 10, 6, 9], 6))
    print(dummy.stockBuySell([3, 3, 5, 0, 0, 3, 1, 4], 8))