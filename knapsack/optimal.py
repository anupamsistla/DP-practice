class Solution:
    def knapsack01(self, wt, val, n, W):
        prev = [0]*(W+1)

        for wei in range(wt[0], W+1):
            prev[wei] = val[0]
        
        for i in range(1, n):
            curr = [0]*(W+1)
            for wei in range(0, W+1):
                notTake = prev[wei]
                take = float("-inf")
                
                if wei >= wt[i]:
                    take = val[i] + prev[wei-wt[i]]
        
                curr[wei] = max(notTake, take)
            prev = curr
        return prev[W]

# Time complexity: O(n*W)
# Space complexity: O(n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.knapsack01([10, 20, 30], [60, 100, 120], 3, 50))
    print(dummy.knapsack01([5, 4, 6, 3], [10, 40, 30, 50], 4, 10))
    print(dummy.knapsack01([1, 2, 3, 8, 7, 4], [20, 5, 10, 40, 15, 25], 6, 10))
    