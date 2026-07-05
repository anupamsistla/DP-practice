class Solution:
    def nonAdjacent(self, nums):
        n = len(nums)
        dp = [-1] * n
        dp[0] = nums[0]
        
        for i in range(1, n):
            pick = nums[i] + dp[i-2] if i >= 2 else nums[i]
            notPick = dp[i-1]
            dp[i] = max(pick, notPick)

        return dp[n-1]
    
if __name__ == "__main__":
    test1 = [2, 1, 4, 9]
    
    tester = Solution()
    print(tester.nonAdjacent(test1))
