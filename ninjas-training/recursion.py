class Solution:
    def foo(self, day, last, matrix):
        maxi = 0

        if day == 0:
            for task in range(3):
                if task != last:
                    maxi = max(maxi, matrix[day][task])
            return maxi
        for task in range(3):
            if task != last:
                points = self.foo(day-1, task, matrix) + matrix[day][task]
                maxi = max(points, maxi)
            
        return maxi

    def ninjaTraining(self, matrix):
        n = len(matrix)
        return self.foo(n-1, 3, matrix)

if __name__ == "__main__":
    test1 = [[10, 40, 70], [20, 50, 80], [30, 60, 90]]
    
    dummy = Solution()
    print(dummy.ninjaTraining(test1))
