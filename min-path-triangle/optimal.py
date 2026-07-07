class Solution:           
    def minTriangleSum(self, triangle):
        n = len(triangle)

        front = [0]*n

        for j in range(n):
            front[j] = triangle[n-1][j]
        
        for i in range(n-2, -1, -1):
            curr = [0]*n
            for j in range(i, -1, -1):
                d = triangle[i][j] + front[j]
                dg = triangle[i][j] + front[j+1]
                curr[j] = min(d, dg)
            
            front = curr
        
        return front[0]

# Time complexity = O(N*N)
# Space complexity = O(N) 

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.minTriangleSum([[1], [1, 2], [1, 2, 4]]))
    print(dummy.minTriangleSum([[1], [4, 7], [4,10, 50], [-50, 5, 6, -100]]))