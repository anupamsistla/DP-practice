from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = float("-inf")
        n = len(heights)
        stack = []

        for i in range(n+1):
            while stack and (i == n or heights[i] <= stack[-1][1]):
                _, height = stack.pop()
                width = 0

                if stack:
                    width = i - stack[-1][0] - 1

                else:
                    width = i
                
                maxArea = max(maxArea, height * width)

            stack.append((i, heights[i] if i < n else float("-inf")))
    
        return maxArea

    def maximalAreaOfSubMatrixOfAll1(self, matrix):
        dp = [0] * len(matrix[0])
        maxArea = float("-inf")

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    dp[j] += 1

                else:
                    dp[j] = 0

                maxArea = max(maxArea, self.largestRectangleArea(dp))
        return maxArea

# Time complexity: O(n * (m + n)) 
# Space complexity: O(m)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.maximalAreaOfSubMatrixOfAll1([[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]))
    print(dummy.maximalAreaOfSubMatrixOfAll1([[1]]))
    print(dummy.maximalAreaOfSubMatrixOfAll1([[1, 0, 1, 0, 0], [1, 0, 1, 1, 1]]))
            