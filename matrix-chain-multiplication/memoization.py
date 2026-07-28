class Solution:
    def foo(self, i, j, nums, dp):
        if dp[i][j] != -1:
            return dp[i][j]

        if i == j:
            return 0

        minOps = float("inf")

        for k in range(i, j):
            steps = nums[i-1] * nums[k] * nums[j] + self.foo(i, k, nums, dp) + self.foo(k+1, j, nums, dp)

            if steps < minOps:
                minOps = steps

        dp[i][j] = minOps
        return dp[i][j]

    def matrixMultiplication(self, nums):
        dp = [[-1]*len(nums) for _ in range(len(nums))]
        return self.foo(1, len(nums)-1, nums, dp)    

# Time complexity: O(n^3) [O(n^2) states + O(n) work in each state]
# Space complexity: O(n^2) + O(n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.matrixMultiplication([10, 20, 30, 40]))
    print(dummy.matrixMultiplication([10, 20, 30, 40, 50]))
    print(dummy.matrixMultiplication([10, 15, 20, 25]))
    print(dummy.matrixMultiplication([4, 2, 3]))
    print(dummy.matrixMultiplication([1, 2, 3, 4, 5]))