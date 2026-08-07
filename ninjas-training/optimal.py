class Solution:                
    def ninjaTraining(self, matrix):
        n = len(matrix)
        prev = [0]*4

        for index in range(3):
            maxPoints = float("-inf")
            for j in range(3):
                if index == j:
                    continue
                maxPoints = max(maxPoints, matrix[0][j])
            prev[index] = maxPoints

        for i in range(1, n):
            curr = [0] * 4            
            for j in range(0, 4):
                maxPoints = float("-inf")
                for index in range(3):
                    if index == j:
                        continue 
                    currPoints = matrix[i][index] + prev[index]
                    maxPoints = max(currPoints, maxPoints)

                curr[j] = maxPoints
            prev = curr
        return prev[3]

# Time complexity: O(n * 4 * 3)
# Space complexity: O(4)

if __name__ == "__main__":
    test1 = [[10, 30, 70], [20, 50, 80], [30, 60, 90]]
    test2 = [[70, 40, 10], [180, 20, 5], [200, 60, 30]]
    test3 = [[20, 10, 10], [20, 10, 10], [20, 30, 10]]

    dummy = Solution()

    print(dummy.ninjaTraining(test1))
    print(dummy.ninjaTraining(test2))
    print(dummy.ninjaTraining(test3))

