class Solution:           
    def minTriangleSum(self, triangle):
        n = len(triangle)

        dp = [[0]*n for _ in range(n)]

        for j in range(n):
            dp[n-1][j] = triangle[n-1][j]

        for i in range(n-2, -1, -1):
            for j in range(i, -1, -1):
                d = triangle[i][j] + dp[i+1][j]
                dg = triangle[i][j] + dp[i+1][j+1]
                dp[i][j] = min(d, dg)
        
        return dp[0][0]

# Time complexity = O(N*N)
# Space complexity = O(N*N) 

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.minTriangleSum([[1], [1, 2], [1, 2, 4]]))
    print(dummy.minTriangleSum([[1], [4, 7], [4,10, 50], [-50, 5, 6, -100]]))