class Solution:
    def foo(self, index, buy, prices, n):
        if index >= n:
            return 0

        profit = 0

        if buy:
            profit = max(-prices[index] + self.foo(index+1, 0, prices, n), self.foo(index+1, 1, prices, n))

        else:
            profit = max(prices[index] + self.foo(index+2, 1, prices, n), self.foo(index+1, 0, prices, n))

        return profit 
            
    def maxProfit(self, prices):
        return self.foo(0, 1, prices, len(prices))

# Time complexity: O(2^n)
# Space complexity: O(n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.maxProfit([1,2,3,0,2]))
    print(dummy.maxProfit([1]))
    print(dummy.maxProfit([3,2,6,5,0,3]))
