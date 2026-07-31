class Solution:
    def foo(self, index, heights, k, dp):
        if dp[index] != -1:
            return dp[index]

        if index == 0:
            return 0

        minCost = float("inf")
        for jump in range(1, k + 1):
            currCost = float("inf")

            if index - jump >= 0:
                currCost = abs(heights[index] - heights[index - jump]) + self.foo(index - jump, heights, k, dp)

            minCost = min(minCost, currCost)

        dp[index] = minCost
        return dp[index]

    def frogJump(self, heights, k):
        n = len(heights)
        dp = [-1]*n

        dp[0] = 0

        for index in range(1, n):
            minCost = float("inf")
            for jump in range(1, k + 1):
                currCost = float("inf")
    
                if index - jump >= 0:
                    currCost = abs(heights[index] - heights[index - jump]) + dp[index - jump]
    
                minCost = min(minCost, currCost)
            dp[index] = minCost

        return dp[n-1]


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