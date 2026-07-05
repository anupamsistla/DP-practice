class Solution:
    def foo(self, index, heights, k):
        if index == 0:
            return 0

        minRes = float("inf")
        for i in range(1, k+1):
            newI = index - i

            if newI >= 0:
                res = self.foo(newI, heights, k) + abs(heights[newI] - heights[index])
                minRes = min(minRes, res)
        
        return minRes

    def frogJump(self, heights, k):
        return self.foo(len(heights)-1, heights,k)
    
if __name__ == "__main__":
    test1 = [10, 5, 20, 0, 15]
    
    
    dummy = Solution()
    res1 = dummy.frogJump(test1, 2)
    print(res1)