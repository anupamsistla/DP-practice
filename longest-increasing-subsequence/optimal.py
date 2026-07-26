class Solution:
    def LIS(self, nums):
        ahead = [0]*(len(nums)+1)
        n = len(nums)

        for index in range(n-1, -1, -1):
            curr = [0]*(len(nums)+1)
            for prevIndex in range(index-1, -2, -1):
                take = 0
                
                if prevIndex == -1 or nums[index] > nums[prevIndex]:
                    take = 1 + ahead[index+1]
        
                notTake = ahead[prevIndex+1]
        
                curr[prevIndex + 1] = max(take, notTake)

            ahead = curr
    
        return ahead[0]
    
if __name__ == "__main__":
    dummy = Solution()
    print(dummy.LIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(dummy.LIS([0, 1, 0, 3, 2, 3]))
    print(dummy.LIS([7, 7, 7, 7, 7, 7, 7]))
    print(dummy.LIS([9, 2, 5, 7]))