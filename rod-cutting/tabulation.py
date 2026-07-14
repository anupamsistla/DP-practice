class Solution:
    def RodCutting(self, price, n):
        dp = [[0]*(n+1) for _ in range(n)]

        for N in range(0, n+1):
            dp[0][N] = N*price[0]
        
        for i in range(1, n):
            for N in range(0, n+1):
                notTake = dp[i-1][N]
                take = float("-inf")
                cuttingLen = i + 1

                if N >= cuttingLen:
                    take = price[i] + dp[i][N-cuttingLen]
        
                dp[i][N] = max(notTake, take)

        return dp[n-1][n]

# Time complexity: O(n^2)
# Space complexity: O(n^2)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.RodCutting([1, 6, 8, 9, 10, 19, 7, 20], 8))
    print(dummy.RodCutting([1, 5, 8, 9], 4))
    print(dummy.RodCutting([5, 5, 8, 9, 10, 17, 17, 20], 8))