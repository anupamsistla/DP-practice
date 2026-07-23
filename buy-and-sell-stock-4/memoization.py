class Solution:
    def foo(self, index, k, arr, n, dp):
        if index == n:
            return 0

        if k == 0:
            return 0

        if dp[index][k] != -1:
            return dp[index][k]
        
        profit = 0

        if k % 2 == 0:
            profit = max(-arr[index] + self.foo(index+1, k-1, arr, n, dp), self.foo(index + 1, k, arr, n, dp))

        else:
            profit = max(arr[index] + self.foo(index + 1, k-1, arr, n, dp), self.foo(index+1, k, arr, n, dp))

        dp[index][k] = profit
        return dp[index][k]
    
    def stockBuySell(self, arr, n, k):
        dp = [[-1]*(2*k+1) for _ in range(n)]
        return self.foo(0, 2*k, arr, n, dp)

# Time complexity: O(n*k)
# Space complexity: O(n*k) + O(n) = O(n*k)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.stockBuySell([4, 2, 7, 1, 11, 5], 6, 2))
    print(dummy.stockBuySell([1, 3, 2, 8, 4, 9], 6, 3))
    print(dummy.stockBuySell([5, 7, 2, 10, 6, 9], 6, 1))
    print(dummy.stockBuySell([3, 3, 5, 0, 0, 3, 1, 4], 8, 3))