class Solution:
    def foo(self, index, k, arr, n):
        if index == n:
            return 0

        if k == 0:
            return 0
        
        profit = 0

        if k % 2 == 0:
            profit = max(-arr[index] + self.foo(index+1, k-1, arr, n), self.foo(index + 1, k, arr, n))

        else:
            profit = max(arr[index] + self.foo(index + 1, k-1, arr, n), self.foo(index+1, k, arr, n))

        return profit
    
    def stockBuySell(self, arr, n, k):
        return self.foo(0, 2*k, arr, n)

# Time complexity: O(2^n)
# Space complexity: O(n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.stockBuySell([4, 2, 7, 1, 11, 5], 6, 2))
    print(dummy.stockBuySell([1, 3, 2, 8, 4, 9], 6, 3))
    print(dummy.stockBuySell([5, 7, 2, 10, 6, 9], 6, 1))
    print(dummy.stockBuySell([3, 3, 5, 0, 0, 3, 1, 4], 8, 3))