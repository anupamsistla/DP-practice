class Solution:
    def foo(self, index, heights, dp, k):
        if index == 0:
            return 0
        
        if dp[index] != -1:
            return dp[index]

        minRes = float("inf")
        for i in range(1, k+1):
            newI = index - i

            if newI >= 0:
                res = self.foo(newI, heights, dp, k) + abs(heights[newI] - heights[index])
                minRes = min(minRes, res)
    
        dp[index] = minRes
        return minRes

    def frogJump(self, heights, k):
        dp = [-1]*len(heights)
        return self.foo(len(heights)-1, heights, dp, k)
    
if __name__ == "__main__":
    test1 = [10, 5, 20, 0, 15]
    test2 = [15, 4, 1, 14, 15]    
    test3 = [15, 4, 1, 14, 15]

    dummy = Solution()
    res1 = dummy.frogJump(test1, 2)
    print(res1)

    res2 = dummy.frogJump(test2, 3)
    print(res2)

    res3 = dummy.frogJump(test3, 4)
    print(res3)