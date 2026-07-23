class Solution:
    def foo(self, index, trans, arr, n, dp):
        if index == n:
            return 0

        if trans == 4:
            return 0

        if dp[index][trans] != -1:
            return dp[index][trans]

        profit = 0

        if trans % 2 == 0:
            profit = max(-arr[index] + self.foo(index + 1, trans + 1, arr, n, dp), self.foo(index + 1, trans, arr, n, dp))

        else:
            profit = max(arr[index] + self.foo(index + 1, trans + 1, arr, n, dp), self.foo(index+1, trans, arr, n, dp))

        dp[index][trans] = profit
        return dp[index][trans]


    def stockBuySell(self, arr, n):
        after = [0]*5 

        for index in range(n-1, -1, -1):
            curr = [0]*5 
            for trans in range(3, -1, -1):
                profit = 0
                
                if trans % 2 == 0:
                    profit = max(-arr[index] + after[trans + 1], after[trans])
        
                else:
                    profit = max(arr[index] + after[trans + 1], after[trans])
        
                curr[trans] = profit
            after = curr

        return after[0]

# Time complexity: O(2^n)
# Space complexity: O(n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.stockBuySell([4, 2, 7, 1, 11, 5], 6))
    print(dummy.stockBuySell([1, 3, 2, 8, 4, 9], 6))
    print(dummy.stockBuySell([5, 7, 2, 10, 6, 9], 6))
    print(dummy.stockBuySell([3, 3, 5, 0, 0, 3, 1, 4], 8))