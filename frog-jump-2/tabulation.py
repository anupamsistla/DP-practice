class Solution:
    def frogJump(self, heights, k):
        dp = [0]*len(heights)
        
        for index in range(1, len(heights)):
            minRes = float("inf")

            for i in range(1, k+1):
                newI = index - i

                if newI >= 0:
                    res = dp[newI] + abs(heights[newI] - heights[index])
                    minRes = min(minRes, res)
            
            dp[index] = minRes

        return dp[-1]    
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