class Solution:
    def foo(self, index, prevIndex, nums, n, dp):
        if index == n:
            return 0

        if dp[index][prevIndex+1] != -1:
            return dp[index][prevIndex+1]

        notTake = self.foo(index+1, prevIndex, nums, n, dp)
        take = float("-inf")

        if prevIndex == -1 or nums[index] % nums[prevIndex] == 0:
            take = 1 + self.foo(index+1, index, nums, n, dp)

        dp[index][prevIndex+1] = max(notTake, take)
        return dp[index][prevIndex+1]

    def largestDivisibleSubset(self, nums):
        nums.sort()
        n = len(nums)
        ahead = [0]*(n+1)

        for index in range(n-1, -1, -1):
            curr = [0]*(n+1)
            for prevIndex in range(index-1, -2, -1):
                notTake = ahead[prevIndex+1]
                take = float("-inf")
        
                if prevIndex == -1 or nums[index] % nums[prevIndex] == 0:
                    take = 1 + ahead[index+1]
        
                curr[prevIndex+1] = max(notTake, take)
            ahead = curr
        
        return ahead[0]
      

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.largestDivisibleSubset([2,4,8,9]))
    print(dummy.largestDivisibleSubset([3, 5, 10, 20]))
    print(dummy.largestDivisibleSubset([16, 8, 2, 4, 32]))
    print(dummy.largestDivisibleSubset([7, 14, 28, 3]))
    print(dummy.largestDivisibleSubset([1, 16, 7, 8, 4]))