class Solution:
    def uniquePaths(self, m, n):
        prev = [0]*n

        for i in range(m):
            curr = [0]*n
            for j in range(n):
                if i == 0 and j == 0:
                    curr[j] = 1
                else:
                    up = prev[j] if i > 0 else 0
                    left = curr[j-1] if j > 0 else 0
                    curr[j] = up + left
            prev = curr

        return curr[n-1]
    
# Time complexity: O(m*n)
# Space complexity: O(n)

if __name__ == "__main__":
    dummy = Solution()
    
    print(dummy.uniquePaths(3, 2))
    print(dummy.uniquePaths(2, 4))