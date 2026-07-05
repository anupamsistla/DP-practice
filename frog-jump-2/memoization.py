class Solution:
    def foo(self, index, heights, k, dp):
        if index == 0:
            return 0
        
        if dp[index] != -1:
            return dp[index]

        minCost = float("inf")
        for i in range(1, k+1):
            newIndex = index - i

            if newIndex >= 0:
                minCost = min(minCost, abs(heights[newIndex] - heights[index]) + self.foo(newIndex, heights, k, dp))
            
        dp[index] = minCost
        return minCost
            
    def frogJump(self, heights, k):
        n = len(heights)-1
        dp = [-1]*(n+1)
        return self.foo(n, heights, k, dp)

# Time complexity: O(n*k)
# Space complexity: O(n + n)
        
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