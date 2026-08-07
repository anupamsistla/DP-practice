class Solution:
    def uniquePaths(self, m, n):
        prev = [0] * m

        for i in range(n):
            curr = [0] * m
            for j in range(m):
                if i == 0 and j == 0:
                    curr[j] = 1

                elif j > 0:
                    curr[j] = prev[j] + curr[j-1]

                else:
                    curr[j] = prev[j]
            prev = curr
        return prev[m-1]
    
if __name__ == "__main__":
    dummy = Solution()
    
    print(dummy.uniquePaths(3, 2))
    print(dummy.uniquePaths(2, 4))
