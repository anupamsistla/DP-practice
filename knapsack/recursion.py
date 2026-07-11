class Solution:
    def foo(self, index, W, wt, val):
        if index == 0:
            if W >= wt[0]:
                return val[0]
            else:
                return 0
        
        notTake = self.foo(index-1, W, wt, val)
        take = float("-inf")

        if W >= wt[index]:
            take = val[index] + self.foo(index-1, W-wt[index], wt, val)
        
        return max(notTake, take)
    
    def knapsack01(self, wt, val, n, W):
        return self.foo(n-1, W, wt, val)
    
# Time complexity: O(2^n)
# Space complexity: O(n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.knapsack01([10, 20, 30], [60, 100, 120], 3, 50))
    print(dummy.knapsack01([5, 4, 6, 3], [10, 40, 30, 50], 4, 10))
    print(dummy.knapsack01([1, 2, 3, 8, 7, 4], [20, 5, 10, 40, 15, 25], 6, 10))
    