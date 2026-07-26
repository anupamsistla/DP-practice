class Solution:
    def LIS(self, nums):
        dp = [1]*len(nums)
        maxI = 1

        for index in range(len(nums)):
            for prevIndex in range(index):
                if nums[prevIndex] < nums[index]:
                    dp[index] = max(dp[index], 1 + dp[prevIndex])

            maxI = max(maxI, dp[index])
        return maxI

# Time complexity: O(n^2)
# Spaace complexity: O(n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.LIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(dummy.LIS([0, 1, 0, 3, 2, 3]))
    print(dummy.LIS([7, 7, 7, 7, 7, 7, 7]))
    print(dummy.LIS([9, 2, 5, 7]))