class Solution:
    def foo(self, i, j, start, target, dp):
        if dp[i][j] != -1:
            return dp[i][j]
        
        if i == 0:
            return j

        if j == 0:
            return i

        if start[i-1] == target[j-1]:
            dp[i][j] = self.foo(i-1, j-1, start, target, dp)
            return dp[i][j]
        
        insert = 1 + self.foo(i, j-1, start, target, dp)
        delete = 1 + self.foo(i-1, j, start, target, dp)
        replace = 1 + self.foo(i-1, j-1, start, target, dp)

        dp[i][j] = min(insert, delete, replace)
        return dp[i][j]

    def editDistance(self, start, target):
        n = len(start)
        m = len(target)
        prev = [0]*(m+1)

        for j in range(m+1):
            prev[j] = j


        for i in range(1, n+1):
            curr = [0] * (m + 1)
            curr[0] = i
            for j in range(1, m+1):
                if start[i-1] == target[j-1]:
                    curr[j] = prev[j-1]

                else:
                    insert = 1 + curr[j-1]
                    delete = 1 + prev[j]
                    replace = 1 + prev[j-1]

                    curr[j] = min(insert, delete, replace)

            prev = curr

        return prev[m]
            

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.editDistance("horse", "ros"))
    print(dummy.editDistance("intention", "execution"))
    print(dummy.editDistance("abcdefg", "azced"))