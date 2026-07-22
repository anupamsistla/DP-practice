class Solution:
    def foo(self, index, buy, arr, n):
        if index == n:
            return 0

        profit = 0

        if buy:
            profit = max(-arr[index] + self.foo(index + 1, 0, arr, n), self.foo(index + 1, 1, arr, n))

        else:
            profit = max(arr[index] + self.foo(index + 1, 1, arr, n), self.foo(index+1, 0, arr, n))

        return profit

    def stockBuySell(self, arr, n):
        return self.foo(0, 1, arr, n)

# Time complexity: O(2^n)
# Space complexity: O(n) 

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.stockBuySell([7, 1, 5, 3, 6, 4], 6))
    print(dummy.stockBuySell([9, 2, 6, 4, 7, 3], 6))
    print(dummy.stockBuySell([2, 3, 4, 5, 6], 5))
    print(dummy.stockBuySell([8, 6, 5, 4, 3], 5))