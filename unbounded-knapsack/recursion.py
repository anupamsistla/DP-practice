class Solution:
    def foo(self, index, W, wt, val):
        if index == 0:
            return W//wt[0] * val[0]

        notTake = self.foo(index-1, W, wt, val)
        take = 0
        
        if W >= wt[index]:
            take = val[index] + self.foo(index, W-wt[index], wt, val)
        
        return max(take, notTake)
    
    def unboundedKnapsack(self, wt, val, n, W):
        return self.foo(n-1, W, wt, val)

# Time complexity: O(2^W/w)
# Space complexity: O(W/w)
# Where 'w' is the smallest weight in the knapsack

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.unboundedKnapsack([2, 4, 6], [5, 11, 13], 3, 10))
    print(dummy.unboundedKnapsack([1, 3, 4, 5], [10, 40, 50, 70], 4, 8))
    print(dummy.unboundedKnapsack([10, 20, 30], [60, 100, 120], 3, 60))
