class Solution:
    # either returns exact position of target in nums or returns the index of the first number greater than target
    def binarySearch(self, target, nums):
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return left

    def LIS(self, nums):
        res = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > res[-1]:
                res.append(nums[i])

            else:
                j = self.binarySearch(nums[i], res)
                res[j] = nums[i]
        return len(res)     
        

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.LIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(dummy.LIS([0, 1, 0, 3, 2, 3]))
    print(dummy.LIS([7, 7, 7, 7, 7, 7, 7]))
    print(dummy.LIS([9, 2, 5, 7]))