class Solution:
    def foo(self, index, buy, cap, arr, n):
        if index == n:
            return 0

        if cap == 0:
            return 0

        profit = 0

        if buy:
            profit = max(-arr[index] + self.foo(index+1, 0, cap, arr, n), self.foo(index+1, 1, cap, arr, n))

        else:
            profit = max(arr[index] + self.foo(index+1, 1, cap-1, arr, n), self.foo(index+1, 0, cap, arr, n))

        return profit
        
    def stockBuySell(self, arr, n):
        return self.foo(0, 1, 2, arr, n)

# Time complexity: O(2^n)
# Space complexity: O(n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.stockBuySell([4, 2, 7, 1, 11, 5], 6))
    print(dummy.stockBuySell([1, 3, 2, 8, 4, 9], 6))
    print(dummy.stockBuySell([5, 7, 2, 10, 6, 9], 6))
    print(dummy.stockBuySell([3, 3, 5, 0, 0, 3, 1, 4], 8))