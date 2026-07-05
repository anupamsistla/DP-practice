class Solution:
    def foo(self, index, nums):
        if index == 0:
            return nums[index]
    
        if index < 0:
            return 0
    
        pick = nums[index] + self.foo(index-2, nums)
        notPick = self.foo(index-1, nums)

        return max(pick, notPick)

    def nonAdjacent(self, nums):
        n = len(nums)
        return self.foo(n-1, nums)
    
if __name__ == "__main__":
    test1 = [2, 1, 4, 9]
    
    tester = Solution()
    print(tester.nonAdjacent(test1))


    