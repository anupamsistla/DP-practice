from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = 0

        for num in nums:
            totalSum += num
        
        if totalSum % 2:
            return False
    
        k = totalSum // 2

        dp = [[False]*(k+1) for _ in range(len(nums))]

        for i in range(len(nums)):
            dp[i][0] = True

        if nums[0] <= k:
            dp[0][nums[0]] = True

        for i in range(1, len(nums)):
            for target in range(1, k+1):
                notTake = dp[i-1][target]
                take = False

                if target >= nums[i]:
                    take = dp[i-1][target-nums[i]]

                dp[i][target] = notTake or take

        return dp[len(nums)-1][k]
    
# Time complexity: O(n*k)
# Space complexity: O(n*k)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.canPartition([2,3,3,3,4,5]))
    print(dummy.canPartition([1, 2, 3, 5]))
        