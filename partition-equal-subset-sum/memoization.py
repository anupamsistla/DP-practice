from typing import List
class Solution:
    def foo(self, index, target, nums, dp):
        if target == 0:
            return True
        
        if dp[index][target] != -1:
            return dp[index][target]
    
        if index == 0:
            return nums[0] == target
    
        notTake = self.foo(index-1, target, nums, dp)
        take = False

        if target >= nums[index]:
            take = self.foo(index-1, target-nums[index], nums, dp)
    
        dp[index][target] = notTake or take
        return dp[index][target]
        
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = 0

        for num in nums:
            totalSum += num
        
        if totalSum % 2:
            return False
    
        k = totalSum // 2

        dp = [[-1]*(k+1) for _ in range(len(nums))]

        return self.foo(len(nums)-1, k, nums, dp)
    
# Time complexity: O(n*k)
# Space complexity: O(n*k + n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.canPartition([2,3,3,3,4,5]))
    print(dummy.canPartition([1, 2, 3, 5]))
        