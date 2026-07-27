class Solution:
    def numberOfLIS(self, nums):
        n = len(nums)
        dp = [1]*n
        cnt = [1]*n
        maxI = 1

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
                    cnt[i] = cnt[j]


                elif nums[i] > nums[j] and 1 + dp[j] == dp[i]:
                    cnt[i] += cnt[j]

            maxI = max(maxI, dp[i])

        res = 0
        for i in range(n):
            if dp[i] == maxI:
                res += cnt[i]

        return res

# Time complexity: O(n^2)
# Space complexity: O(n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.numberOfLIS([1, 3, 5, 4, 7]))
    print(dummy.numberOfLIS([2, 2, 2, 2, 2]))
    print(dummy.numberOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(dummy.numberOfLIS([1, 3, 1, 2, 7]))
