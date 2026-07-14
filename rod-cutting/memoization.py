class Solution:
    def foo(self, index, n, price, dp):
        if dp[index][n] != -1:
            return dp[index][n]
        
        if index == 0:
            return n*price[0]

        notTake = self.foo(index-1, n, price, dp)
        take = float("-inf")
        cuttingLen = index + 1

        if n >= cuttingLen:
            take = price[index] + self.foo(index, n-cuttingLen, price, dp)
        
        dp[index][n] = max(notTake, take)
        return dp[index][n]

    def RodCutting(self, price, n):
        dp = [[-1]*(n+1) for _ in range(n)]
        return self.foo(n-1, n, price, dp)

# Time complexity: O(n^2)
# Space complexity: O(n^2 + n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.RodCutting([1, 6, 8, 9, 10, 19, 7, 20], 8))
    print(dummy.RodCutting([1, 5, 8, 9], 4))
    print(dummy.RodCutting([5, 5, 8, 9, 10, 17, 17, 20], 8))