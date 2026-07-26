# Testing myself with returning the length of the longest divisible subset not a STRIVER question
class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()
        ahead = [0]*(len(nums)+1)
        n = len(nums)

        for index in range(n-1, -1, -1):
            curr = [0]*(len(nums)+1)
            for prevIndex in range(index-1, -2, -1):
                take = 0
                if prevIndex == -1 or nums[index] % nums[prevIndex] == 0:
                    take = 1 + ahead[index + 1]
        
                notTake = ahead[prevIndex + 1]
                curr[prevIndex + 1] = max(take, notTake)
                
            ahead = curr
        return ahead[0]

# Time complexity: O(n^2)
# Space complexity: O(n)
 
if __name__ == "__main__":
    dummy = Solution()
    print(dummy.largestDivisibleSubset([3, 5, 10, 20]))
    print(dummy.largestDivisibleSubset([16, 8, 2, 4, 32]))
    print(dummy.largestDivisibleSubset([7, 14, 28, 3]))
    print(dummy.largestDivisibleSubset([1, 16, 7, 8, 4]))