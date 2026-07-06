class Solution:
    def foo(self, i, j):
        if i == 0 and j == 0:
            return 1
    
        if i < 0 or j < 0:
            return 0

        up = self.foo(i-1, j)
        left = self.foo(i, j-1)
        return up + left


    def uniquePaths(self, m, n):
        return self.foo(m-1, n-1)

# Time complexity: O(2^(m*n))
# Space complexity: Path length = O(m-1 + n-1) = O(m+n)


if __name__ == "__main__":
    dummy = Solution()
    
    print(dummy.uniquePaths(3, 2))
    print(dummy.uniquePaths(2, 4))