class Solution:
    def targetSum(self, n, target, nums):
        totalSum = sum(nums)
        dp = [[0]*(totalSum+1) for _ in range(n)]
        
        for i in range(n):
            dp[i][0] = 1
        
        dp[0][nums[0]] = 1

        for i in range(1, len(nums)):
            for k in range(1, totalSum+1):
                notTake = dp[i-1][k]
                take = 0

                if k >= nums[i]:
                    take = dp[i-1][k - nums[i]]
        
                dp[i][k] = notTake + take

        
    
# Time complexity: O(n * totalSum)
# Space complexity: O(n * totalSum)
    
if __name__ == "__main__":
    dummy = Solution()
    print(dummy.targetSum(5, 3, [1, 1, 1, 1, 1],))
                    