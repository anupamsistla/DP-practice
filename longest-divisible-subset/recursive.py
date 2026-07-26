# Testing myself with returning the length of the longest divisible subset not a STRIVER question
class Solution:
    def foo(self, index, prevIndex, nums, n):
        if index == n:
            return 0

        take = 0
        if prevIndex == -1 or nums[index] % nums[prevIndex] == 0:
            take = 1 + self.foo(index + 1, index, nums, n)

        notTake = self.foo(index+1, prevIndex, nums, n)
        return max(take, notTake)

    def largestDivisibleSubset(self, nums):
        nums.sort()
        return self.foo(0, -1, nums, len(nums))

# Time complexity: O(2^n)
# Space complexity: O(n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.largestDivisibleSubset([3, 5, 10, 20]))
    print(dummy.largestDivisibleSubset([16, 8, 2, 4, 32]))
    print(dummy.largestDivisibleSubset([7, 14, 28, 3]))
    print(dummy.largestDivisibleSubset([1, 16, 7, 8, 4]))