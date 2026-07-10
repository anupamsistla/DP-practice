from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = 0

        for num in nums:
            totalSum += num
        
        if totalSum % 2:
            return False
    
        k = totalSum // 2

        prev = [False]*(k+1)
        prev[0] = True

        if nums[0] <= k:
            prev[nums[0]] = True

        for i in range(1, len(nums)):
            temp = [False]*(k+1)
            temp[0] = True
            for target in range(1, k+1):
                notTake = prev[target]
                take = False

                if target >= nums[i]:
                    take = prev[target-nums[i]]

                temp[target] = notTake or take
            prev = temp

        return prev[k]
    
# Time complexity: O(n*k)
# Space complexity: O(k)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.canPartition([2,3,3,3,4,5]))
    print(dummy.canPartition([1, 2, 3, 5]))