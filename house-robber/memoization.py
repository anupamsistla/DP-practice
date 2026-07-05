class Solution:
    def foo(self, index, nums, dp):
        if index < 0:
            return 0
    
        inc = nums[index] + self.foo(index-2, nums, dp)
        exc = self.foo(index-1, nums, dp)
        dp[index] = max(inc, exc)
        
        return dp[index]

    def nonAdjacent(self, nums):
        n = len(nums)
        dp = [-1]*n
        
        return self.foo(n-1, nums, dp)
    
# Time complexity: O(n)
# Space complexity: O(n + n)

if __name__ == "__main__":
    dummy = Solution()

    print(dummy.nonAdjacent([1, 2, 4]))
    print(dummy.nonAdjacent([2, 1, 4, 9]))

