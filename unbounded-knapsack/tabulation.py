class Solution:
    def unboundedKnapsack(self, wt, val, n, W):
        dp = [[0]*(W+1) for _ in range(len(wt))]
        for w in range(W+1):
            dp[0][w] = w//wt[0]*val[0]
        
        for i in range(1, n):
            for w in range(W+1):
                notTake = dp[i-1][w]
                take = 0

                if w >= wt[i]:
                    take = val[i] + dp[i][w-wt[i]]
                
                dp[i][w] = max(notTake, take)

        return dp[n-1][W]

# Time complexity: O(n*W)
# Space complexity: O(n*W)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.unboundedKnapsack([2, 4, 6], [5, 11, 13], 3, 10))
    print(dummy.unboundedKnapsack([1, 3, 4, 5], [10, 40, 50, 70], 4, 8))
    print(dummy.unboundedKnapsack([10, 20, 30], [60, 100, 120], 3, 60))
