class Solution:
    def foo(self, i, j, n, triangle):
        if i == n-1:
            return triangle[i][j]
        
        d = triangle[i][j] + self.foo(i+1, j, n, triangle)
        dg = triangle[i][j] + self.foo(i+1, j+1, n, triangle)
        
        return min(d, dg)
    
    def minTriangleSum(self, triangle):
       n = len(triangle)
       return self.foo(0, 0, n, triangle)

# Time complexity = O(2^(n-1)) = O(2^n)
# Space complexity = O(N) 

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.minTriangleSum([[1], [1, 2], [1, 2, 4]]))
    print(dummy.minTriangleSum([[1], [4, 7], [4,10, 50], [-50, 5, 6, -100]]))
    