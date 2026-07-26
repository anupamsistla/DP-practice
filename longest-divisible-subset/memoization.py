# Testing myself with returning the length of the longest divisible subset not a STRIVER question
class Solution:
    def foo(self, index, prevIndex, nums, n, dp):
        if index == n:
            return 0

        if dp[index][prevIndex + 1] != -1:
            return dp[index][prevIndex + 1]

        take = 0
        if prevIndex == -1 or nums[index] % nums[prevIndex] == 0:
            take = 1 + self.foo(index + 1, index, nums, n, dp)

        notTake = self.foo(index+1, prevIndex, nums, n, dp)
        dp[index][prevIndex + 1] = max(take, notTake)

        return dp[index][prevIndex + 1]
        
    def largestDivisibleSubset(self, nums):
        nums.sort()
        dp = [[-1]*(len(nums)+1) for _ in range(len(nums))]
        return self.foo(0, -1, nums, len(nums), dp)

# Time complexity: O(n^2)
# Space complexity: O(n^2) + O(n) = O(n)
 
if __name__ == "__main__":
    dummy = Solution()
    print(dummy.largestDivisibleSubset([3, 5, 10, 20]))
    print(dummy.largestDivisibleSubset([16, 8, 2, 4, 32]))
    print(dummy.largestDivisibleSubset([7, 14, 28, 3]))
    print(dummy.largestDivisibleSubset([1, 16, 7, 8, 4]))