class Solution:
    def nonAdjacent(self, nums):
        n = len(nums)
        prev2, prev = 0, nums[0]
        
        for i in range(1, n):
            pick = nums[i] + prev2
            notPick = prev
            prev2 = prev
            prev = max(pick, notPick)

        return prev
    
if __name__ == "__main__":
    test1 = [2, 1, 4, 9]
    
    tester = Solution()
    print(tester.nonAdjacent(test1))
