class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        i, j = n, m
        res = ""

        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                res = str1[i-1] + res
                i -= 1
                j -= 1

            else:
                if dp[i-1][j] >= dp[i][j-1]:
                    res = str1[i-1] + res
                    i -= 1

                else:
                    res = str2[j-1] + res
                    j -= 1
        return str1[:i] + str2[:j] + res
        

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.shortestCommonSupersequence("brute", "groot"))
    print(dummy.shortestCommonSupersequence("mno", "nop"))
    print(dummy.shortestCommonSupersequence("dynamic","program"))
    print(dummy.shortestCommonSupersequence("coding", "ninjas"))