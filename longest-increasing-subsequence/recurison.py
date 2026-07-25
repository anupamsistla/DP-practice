class Solution:
    def foo(self, index, prevIndex, nums, n):
        if index == n:
            return 0

        take = 0

        if prevIndex == -1 or nums[index] > nums[prevIndex]:
            take = 1 + self.foo(index+1, index, nums, n)

        notTake = self.foo(index+1, prevIndex, nums, n)
        return max(take, notTake)
    
    def LIS(self, nums):
        return self.foo(0, -1, nums, len(nums))


if __name__ == "__main__":
    dummy = Solution()
    print(dummy.LIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(dummy.LIS([0, 1, 0, 3, 2, 3]))
    print(dummy.LIS([7, 7, 7, 7, 7, 7, 7]))
    print(dummy.LIS([9, 2, 5, 7]))