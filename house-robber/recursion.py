class Solution:
    def foo(self, index, nums):
        if index < 0:
            return 0
    
        inc = nums[index] + self.foo(index-2, nums)
        exc = self.foo(index-1, nums)
        return max(inc, exc)

    def nonAdjacent(self, nums):
        n = len(nums)
        
        return self.foo(n-1, nums)
    
# Time complexity: O(2^n)
# Space complexity: O(n)

if __name__ == "__main__":
    dummy = Solution()

    print(dummy.nonAdjacent([1, 2, 4]))
    print(dummy.nonAdjacent([2, 1, 4, 9]))

