from typing import List
class Solution:
    def foo(self, index, target, nums):
        if target == 0:
            return True
    
        if index == 0:
            return nums[0] == target
    
        notTake = self.foo(index-1, target, nums)
        take = False

        if target >= nums[index]:
            take = self.foo(index-1, target-nums[index], nums)
        
        return take or notTake

    def canPartition(self, nums: List[int]) -> bool:
        totalSum = 0
        
        for num in nums:
            totalSum += num
        
        if totalSum % 2:
            return False
    
        k = totalSum//2

        return self.foo(len(nums)-1, k, nums)
    
# Time complexity: O(2^n)
# Space complexity: O(n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.canPartition([2,3,3,3,4,5]))
    print(dummy.canPartition([1, 2, 3, 5]))
        
        