class Solution:
    def foo(self, index, last, matrix, dp):
        toRet = 0
        if index == 0:
            for i in range(3):
                if i != last:
                    toRet = max(toRet, matrix[index][i])
            return toRet
        
        if dp[index][last] != -1:
            return dp[index][last]
        
        for i in range(3):
            if i != last:
                toRet = max(toRet, matrix[index][i] + self.foo(index-1, i, matrix, dp))

        dp[index][last] = toRet
        return toRet
    
    def ninjaTraining(self, matrix):
        n = len(matrix)-1
        dp = [[-1]*4 for _ in range(n+1)]

        return self.foo(n, 3, matrix, dp)
         
# Time complexity: O(n * 4 * 3)
# Space complexity: O(n * 4 + n)


if __name__ == "__main__":
    test1 = [[10, 30, 70], [20, 50, 80], [30, 60, 90]]
    test2 = [[70, 40, 10], [180, 20, 5], [200, 60, 30]]
    test3 = [[20, 10, 10], [20, 10, 10], [20, 30, 10]]

    dummy = Solution()

    print(dummy.ninjaTraining(test1))
    print(dummy.ninjaTraining(test2))
    print(dummy.ninjaTraining(test3))

