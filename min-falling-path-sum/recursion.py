class Solution:
    def foo(self, i, j, matrix):
        if j < 0 or j >= len(matrix[0]):
            return float("inf")

        if i == 0:
            return matrix[0][j]

        one = matrix[i][j] + self.foo(i-1, j-1, matrix)
        two = matrix[i][j] + self.foo(i-1, j, matrix)
        three = matrix[i][j] + self.foo(i-1, j+1, matrix)
        return min(one, two, three)

    def minPathSum(self, matrix):
        n = len(matrix)
        minSum = float("inf")

        for j in range(len(matrix[0])):
            minSum = min(minSum, self.foo(n-1, j, matrix))

        return minSum

# Time complexity: O(3^n)
# Space complexity: O(n)

if __name__ == "__main__":
    dummy = Solution()

    print(dummy.minPathSum([[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]))
    print(dummy.minPathSum([[1, 4, 3, 1], [2, 3, -1, -1], [1, 1, -1, 8]]))
    print(dummy.minPathSum([[4, 3, 4], [4, 5, 1], [4, 6, 2], [4, 1, 4]]))