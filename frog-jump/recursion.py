class Solution:
    def foo(self, index, heights):
        if index == 0:
            return 0

        one = abs(heights[index-1] - heights[index]) + self.foo(index-1, heights)
        
        two = float("inf")
        if index >= 2:
            two = abs(heights[index-2] - heights[index]) + self.foo(index-2, heights)

        return min(one, two)
        
    def frogJump(self, heights):
        n = len(heights)-1
        return self.foo(n, heights)

# Time complexity: O(2^n)
# Space complexity: O(n)
    
if __name__ == "__main__":
    dummy = Solution()
    
    print(dummy.frogJump([2, 1, 3, 5, 4]))
    print(dummy.frogJump([7, 5, 1, 2, 6]))

        