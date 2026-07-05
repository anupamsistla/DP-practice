class Solution:
    def foo(self, day, last, matrix, dp):
        maxi = 0
        if day == 0:
            for task in range(3):
                if task != last:
                    maxi = max(maxi, matrix[day][task])
            return maxi
        if dp[day][last] != -1:
            return dp[day][last]
    
        for task in range(3):
            if task != last:
                points = self.foo(day-1, task, matrix) + matrix[day][task]
                maxi = max(maxi, points)
        dp[day][last] = maxi
        
    def ninjaTraining(self, matrix):
        n = len(matrix)
        dp  = [[-1]*4 for i in range(n)]
        return self.foo(n-1, 3, matrix, dp)

if __name__ == "__main__":
    test1 = [[10, 40, 70], [20, 50, 80], [30, 60, 90]]
    test2 = [[2, 1, 3], [3, 4, 6], [10, 1, 6], [8, 3, 7]]
    
    dummy = Solution()
    print(dummy.ninjaTraining(test1))
    print(dummy.ninjaTraining(test2))
