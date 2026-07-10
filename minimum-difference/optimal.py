from typing import List
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        totalSum = 0
        for num in nums:
            totalSum += num
        
        k = totalSum // 2
        
        prev = [False]*(k+1)

        prev[0] = True
        
        prev[nums[0]] = True

        for i in range(1, len(nums)):
            curr = [False]*(k+1)
            curr[0] = True
            for target in range(1, k + 1):
                take = prev[target]
                notTake = False

                if target >= nums[i]:
                    notTake = prev[target-nums[i]]

                curr[target] = take or notTake
            
            prev = curr
        
        minDiff = float("inf")
        for i in range(k+1):
            if curr[i] == True:
                minDiff = min(minDiff, abs((totalSum - i) - i))
        
        return minDiff
    
# Time complexity: O(n*k)
# Space complexity: O(k)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.minimumDifference([3, 2, 7]))
    print(dummy.minimumDifference([1, 2, 3, 4, 5]))