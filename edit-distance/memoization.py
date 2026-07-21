class Solution:
    def foo(self, i, j, start, target, dp):
        if i < 0:
            return j + 1
        
        if j < 0:
            return i + 1
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        if start[i] == target[j]:
            dp[i][j] = self.foo(i-1, j-1, start, target, dp)
            return dp[i][j]

        insert = 1 + self.foo(i, j-1, start, target, dp)
        delete = 1 + self.foo(i-1, j, start, target, dp)
        replace = 1 + self.foo(i-1, j-1, start, target, dp)

        dp[i][j] = min(insert, delete, replace)
        return dp[i][j]
    

    def editDistance(self, start, target):
        n, m = len(start), len(target)
        dp = [[-1]*m for _ in range(n)]
        return self.foo(n-1, m-1, start, target, dp)        
        
# Time complexity: O(n*m)
# Space complexity: O(n*m) + O(n+m)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.editDistance("horse", "ros"))
    print(dummy.editDistance("intention", "execution"))
    print(dummy.editDistance("abcdefg", "azced"))
