class Solution:
    def knapsack01(self, wt, val, n, W):
        dp = [[0]*(W+1) for _ in range(n)]

        for wei in range(wt[0], W+1):
            dp[0][wei] = val[0]
        
        for i in range(1, n):
            for wei in range(0, W+1):
                notTake = dp[i-1][wei]
                take = float("-inf")
                
                if wei >= wt[i]:
                    take = val[i] + dp[i-1][wei-wt[i]]
        
                dp[i][wei] = max(notTake, take)
        
        return dp[n-1][W]

# Time complexity: O(n*W)
# Space complexity: O(n*W)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.knapsack01([10, 20, 30], [60, 100, 120], 3, 50))
    print(dummy.knapsack01([5, 4, 6, 3], [10, 40, 30, 50], 4, 10))
    print(dummy.knapsack01([1, 2, 3, 8, 7, 4], [20, 5, 10, 40, 15, 25], 6, 10))
    