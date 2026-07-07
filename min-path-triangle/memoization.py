class Solution:
    def foo(self, i, j, n, triangle, dp):
        if i == n-1:
            return triangle[i][j]

        if dp[i][j] != -1:
            return dp[i][j]
        
        d = triangle[i][j] + self.foo(i+1, j, n, triangle, dp)
        dg = triangle[i][j] + self.foo(i+1, j+1, n, triangle, dp)
        
        dp[i][j] = min(d, dg) 
        return dp[i][j]
           
    def minTriangleSum(self, triangle):
       n = len(triangle)
       dp = [[-1]*n for _ in range(n)]

       return self.foo(0, 0, n, triangle, dp)

# Time complexity = O(N*N)
# Space complexity = O(N + N*N) = O(N*N) 

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.minTriangleSum([[1], [1, 2], [1, 2, 4]]))
    print(dummy.minTriangleSum([[1], [4, 7], [4,10, 50], [-50, 5, 6, -100]]))
    