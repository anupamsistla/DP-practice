class Solution:
    def foo(self, index, nums, dp):
        if index == 0:
            return nums[index]
    
        if index < 0:
            return 0
        
        if dp[index] != -1: return dp[index]
    
        pick = nums[index] + self.foo(index-2, nums, dp)
        notPick = self.foo(index-1, nums, dp)

        dp[index] = max(pick, notPick)
        return dp[index]

    def nonAdjacent(self, nums):
        n = len(nums)
        dp = [-1] * n
        return self.foo(n-1, nums, dp)
    
if __name__ == "__main__":
    test1 = [2, 1, 4, 9]
    
    tester = Solution()
    print(tester.nonAdjacent(test1))
