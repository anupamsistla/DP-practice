from typing import List
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        totalSum = 0
        for num in nums:
            totalSum += num
        
        dp = [[False]*(totalSum+1) for _ in range(len(nums))]

        for i in range(len(nums)):
            dp[i][0] = True
        
        dp[0][nums[0]] = True

        for i in range(1, len(nums)):
            for target in range(1, totalSum + 1):
                take = dp[i-1][target]
                notTake = False

                if target >= nums[i]:
                    notTake = dp[i-1][target-nums[i]]

                dp[i][target] = take or notTake
        
        minDiff = float("inf")
        n = len(nums)

        for i in range(totalSum // 2 + 1):
            if dp[n-1][i] == True:
                minDiff = min(minDiff, totalSum - i - i)
        
        return minDiff


# Time complexity: O(n * totalSum)
# Space complexity: O(n * totalSum) 

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.minimumDifference([3, 2, 7]))
    print(dummy.minimumDifference([1, 2, 3, 4, 5]))