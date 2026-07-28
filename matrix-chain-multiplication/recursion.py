class Solution:
    def foo(self, i, j, nums):
        if i == j:
            return 0

        minOps = float("inf")

        for k in range(i, j):
            steps = nums[i-1] * nums[k] * nums[j] + self.foo(i, k, nums) + self.foo(k+1, j, nums)

            if steps < minOps:
                minOps = steps

        return minOps
    
    def matrixMultiplication(self, nums):
        return self.foo(1, len(nums)-1, nums)    

# Time complexity: Exponential
# Space complexity: O(n)


if __name__ == "__main__":
    dummy = Solution()
    print(dummy.matrixMultiplication([10, 20, 30, 40]))
    print(dummy.matrixMultiplication([10, 20, 30, 40, 50]))
    print(dummy.matrixMultiplication([10, 15, 20, 25]))
    print(dummy.matrixMultiplication([4, 2, 3]))
    print(dummy.matrixMultiplication([1, 2, 3, 4, 5]))