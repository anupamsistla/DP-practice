class Solution:  
    def frogJump(self, heights):
        n = len(heights)-1

        prev2, prev1 = 0, 0
        for i in range(1, n+1):
            one = abs(heights[i-1] - heights[i]) + prev1

            two = float("inf")
            if i >= 2:
                two = abs(heights[i-2] - heights[i]) + prev2

            prev2 = prev1
            prev1 = min(one, two)

        return prev1

# Time complexity: O(n)
# Space complexity: O(1)
    
if __name__ == "__main__":
    dummy = Solution()
    
    print(dummy.frogJump([2, 1, 3, 5, 4]))
    print(dummy.frogJump([7, 5, 1, 2, 6]))
