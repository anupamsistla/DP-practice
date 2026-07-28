class Solution:
    def matrixMultiplication(self, nums):
        n = len(nums)
        dp = [[0]*n for _ in range(n)]

        for i in range(n-1, 0, -1):
            for j in range(i+1, n):
                minOps = float("inf")
                
                for k in range(i, j):
                    steps = nums[i-1] * nums[k] * nums[j] + dp[i][k] + dp[k+1][j]
        
                    if steps < minOps:
                        minOps = steps
        
                dp[i][j] = minOps

        return dp[1][len(nums)-1]    

# Time complexity: O(n^3)
# Space complexity: O(n^2)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.matrixMultiplication([10, 20, 30, 40]))
    print(dummy.matrixMultiplication([10, 20, 30, 40, 50]))
    print(dummy.matrixMultiplication([10, 15, 20, 25]))
    print(dummy.matrixMultiplication([4, 2, 3]))
    print(dummy.matrixMultiplication([1, 2, 3, 4, 5]))