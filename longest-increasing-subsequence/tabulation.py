class Solution:
    def LIS(self, nums):
        dp = [[0]*(len(nums)+1) for _ in range(len(nums)+1)]
        n = len(nums)

        for index in range(n-1, -1, -1):
            for prevIndex in range(index-1, -2, -1):
                take = 0
                
                if prevIndex == -1 or nums[index] > nums[prevIndex]:
                    take = 1 + dp[index+1][index+1]
        
                notTake = dp[index+1][prevIndex+1]
        
                dp[index][prevIndex + 1] = max(take, notTake)
    
        return dp[0][0]
    
if __name__ == "__main__":
    dummy = Solution()
    print(dummy.LIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(dummy.LIS([0, 1, 0, 3, 2, 3]))
    print(dummy.LIS([7, 7, 7, 7, 7, 7, 7]))
    print(dummy.LIS([9, 2, 5, 7]))