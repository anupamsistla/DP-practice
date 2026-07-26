class Solution:
    def LIS(self, nums):
        dp = [1]*len(nums)
        hash = [i for i in range(len(nums))]
        lastIndex = 0
        maxI = 1

        for index in range(len(nums)):
            for prevIndex in range(index):
                if nums[prevIndex] < nums[index] and (1 + dp[prevIndex] > dp[index]):
                    dp[index] = 1 + dp[prevIndex]
                    hash[index] = prevIndex

            if dp[index] > maxI:
                maxI = dp[index]
                lastIndex = index

        toRet = []
        while hash[lastIndex] != lastIndex:
            toRet.append(nums[lastIndex])
            lastIndex = hash[lastIndex]

        toRet.append(nums[lastIndex])
        toRet.reverse()
        return toRet

# Time complexity: O(n^2)
# Spaace complexity: O(n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.LIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(dummy.LIS([0, 1, 0, 3, 2, 3]))
    print(dummy.LIS([7, 7, 7, 7, 7, 7, 7]))
    print(dummy.LIS([9, 2, 5, 7]))