class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()
        dp = [1]*len(nums) 
        hash = [i for i in range(len(nums))]
        maxI = 1
        lastIndex = 0

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
                    hash[i] = j

            if dp[i] > maxI:
                maxI = dp[i]
                lastIndex = i

        res = []
        while hash[lastIndex] != lastIndex:
            res.append(nums[lastIndex])
            lastIndex = hash[lastIndex]

        res.append(nums[lastIndex])
        return res

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.largestDivisibleSubset([3, 5, 10, 20]))
    print(dummy.largestDivisibleSubset([16, 8, 2, 4, 32]))
    print(dummy.largestDivisibleSubset([7, 14, 28, 3]))
    print(dummy.largestDivisibleSubset([1, 16, 7, 8, 4]))