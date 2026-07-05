class Solution:
    def nonAdjacent(self, nums):
        n = len(nums)
        dp = [-1]*n

        dp[0] = nums[0]

        for i in range(1, n):
            inc = nums[i] + dp[i-2] if i >= 2 else nums[i]
            exc = dp[i-1]
            dp[i] = max(inc, exc)
        
        return dp[n-1]
    
# Time complexity: O(n)
# Space complexity: O(n)

if __name__ == "__main__":
    dummy = Solution()

    print(dummy.nonAdjacent([1, 2, 4]))
    print(dummy.nonAdjacent([2, 1, 4, 9]))
