class Solution:
    def foo(self, index, prevIndex, nums, n, dp):
        if index == n:
            return 0

        if dp[index][prevIndex + 1] != -1:
            return dp[index][prevIndex + 1]

        take = 0

        if prevIndex == -1 or nums[index] > nums[prevIndex]:
            take = 1 + self.foo(index+1, index, nums, n, dp)

        notTake = self.foo(index+1, prevIndex, nums, n, dp)

        dp[index][prevIndex + 1] = max(take, notTake)
        return dp[index][prevIndex + 1]
    
    def LIS(self, nums):
        dp = [[-1]*(len(nums)+1) for _ in range(len(nums))]
        return self.foo(0, -1, nums, len(nums), dp)
    
if __name__ == "__main__":
    dummy = Solution()
    print(dummy.LIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(dummy.LIS([0, 1, 0, 3, 2, 3]))
    print(dummy.LIS([7, 7, 7, 7, 7, 7, 7]))
    print(dummy.LIS([9, 2, 5, 7]))