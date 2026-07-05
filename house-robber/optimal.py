class Solution:
    def nonAdjacent(self, nums):
        n = len(nums)
        prev2, prev1 = 0, nums[0]

        for i in range(1, n):
            inc = nums[i] + prev2
            exc = prev1
            prev2 = prev1
            prev1 = max(inc, exc)
        
        return prev1
    
# Time complexity: O(n)
# Space complexity: O(1)

if __name__ == "__main__":
    dummy = Solution()

    print(dummy.nonAdjacent([1, 2, 4]))
    print(dummy.nonAdjacent([2, 1, 4, 9]))
