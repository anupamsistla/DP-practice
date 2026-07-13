class Solution:
    def foo(self, index, W, wt, val, dp):
        if dp[index][W] != -1:
            return dp[index][W]

        if index == 0:
            return W//wt[0] * val[0]
    
        notTake = self.foo(index-1, W, wt, val, dp)
        take = 0

        if W >= wt[index]:
            take = val[index] + self.foo(index, W-wt[index], wt, val, dp)
        
        dp[index][W] = max(notTake, take)
        return dp[index][W]
    
    def unboundedKnapsack(self, wt, val, n, W):
        dp = [[-1]*(W+1) for _ in range(len(wt))]
        return self.foo(n-1, W, wt, val, dp)

# Time complexity: O(n*W)
# Space complexity: O(n*W) + O(W/w) = O(n*W)
# Where 'w' is the smallest weight in the knapsack

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.unboundedKnapsack([2, 4, 6], [5, 11, 13], 3, 10))
    print(dummy.unboundedKnapsack([1, 3, 4, 5], [10, 40, 50, 70], 4, 8))
    print(dummy.unboundedKnapsack([10, 20, 30], [60, 100, 120], 3, 60))
