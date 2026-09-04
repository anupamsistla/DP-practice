class Solution:
    def foo(self, index, wt, val, n, W, dp):
        if dp[index][W] != -1:
            return dp[index][W]
        
        if index == 0:
            if W >= wt[index]:
                return val[index]
            else:
                return 0

        notTake = self.foo(index-1, wt, val, n, W, dp)
        take = float("-inf")

        if W >= wt[index]:
            take = val[index] + self.foo(index-1, wt, val, n, W-wt[index], dp)

        dp[index][W] = max(notTake, take)
        return dp[index][W]
        
    def knapsack01(self, wt, val, n, W):
        prev = [0]*(W+1)

        for w in range(W+1):
            if w >= wt[0]:
                prev[w] = val[0]


        for index in range(1, n):
            curr = [0]*(W+1)
            for w in range(W+1):
                notTake = prev[w]
                take = float("-inf")
        
                if w >= wt[index]:
                    take = val[index] + prev[w-wt[index]]
        
                curr[w] = max(notTake, take)
            prev = curr
        
        return prev[W]

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.knapsack01([10, 20, 30], [60, 100, 120], 3, 50))
    print(dummy.knapsack01([5, 4, 6, 3], [10, 40, 30, 50], 4, 10))
    print(dummy.knapsack01([1, 2, 3, 8, 7, 4], [20, 5, 10, 40, 15, 25], 6, 10))
    