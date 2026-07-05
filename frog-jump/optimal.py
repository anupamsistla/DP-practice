class Solution:
    def foo(self, index, heights):
        if index == 0:
            return 0

        left = self.foo(index-1, heights) + abs(heights[index-1] - heights[index])
        right = float("inf")

        if index >= 2:
            right = self.foo(index-2, heights) + abs(heights[index-2] - heights[index])

        return min(left, right)
    
    def frogJump(self, heights):
        prev1, prev2 = 0, 0 
        for i in range(1,len(heights)):
            left = prev1 + abs(heights[i-1]- heights[i])
            right = float("inf")

            if i >= 2:
                right = prev2 + abs(heights[i-2] - heights[i])
            
            prev2 = prev1
            prev1 = min(left, right)
        return prev2
if __name__ == "__main__":
    test1 = [10, 20, 30, 10]
    test2 = [30, 10, 60, 10, 60, 50]
    
    dummy = Solution()
    res1 = dummy.frogJump(test1)
    print(res1)