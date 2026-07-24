class Solution:
    def foo(self, index, buy, fee, arr, n):
        if index == n:
            return 0

        profit = 0

        if buy: 
            profit = max(-arr[index] + self.foo(index+1, 0, fee, arr, n), self.foo(index + 1, 1, fee, arr, n))

        else:
            profit = max(arr[index] + self.foo(index+1, 1, fee, arr, n) - fee, self.foo(index+1, 0, fee, arr, n))

        return profit

    def stockBuySell(self, arr, n, fee):
        return self.foo(0, 1, fee, arr, n)

# Time complexity: O(2^n)
# Space complexity: O(n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.stockBuySell([1, 3, 4, 0, 2], 5, 1))
    print(dummy.stockBuySell([1, 3, 2, 8, 4, 9], 6, 2))
    print(dummy.stockBuySell([10, 3, 7, 5, 1, 3], 6, 3))
