class Solution:
    def foo(self, index, buy, prices, n, dp):
        if index >= n:
            return 0

        if dp[index][buy] != -1:
            return dp[index][buy]

        profit = 0

        if buy:
            profit = max(-prices[index] + self.foo(index+1, 0, prices, n, dp), self.foo(index+1, 1, prices, n, dp))

        else:
            profit = max(prices[index] + self.foo(index+2, 1, prices, n, dp), self.foo(index+1, 0, prices, n, dp))

        dp[index][buy] = profit 
        return dp[index][buy]
            
    def maxProfit(self, prices):
        dp = [[-1]*2 for _ in range(len(prices))]

        return self.foo(0, 1, prices, len(prices), dp)

# Time complexity: O(n*2)
# Space complexity: O(n*2) + O(n) = O(n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.maxProfit([1,2,3,0,2]))
    print(dummy.maxProfit([1]))
    print(dummy.maxProfit([3,2,6,5,0,3]))
