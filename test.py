class Solution:
    def foo(self, i, rodLength, price, dp):
        if i == 0:
            if (i + 1) <= rodLength:
                return price[0]*rodLength

            else:
                return 0

        if dp[i][rodLength] != -1:
            return dp[i][rodLength]

        notTake = self.foo(i-1, rodLength, price, dp)
        take = float("-inf")

        if rodLength >= (i+1):
            take = price[i] + self.foo(i, rodLength - (i+1), price, dp)

        dp[i][rodLength] = max(notTake, take)
        return dp[i][rodLength]

    def RodCutting(self, price, n):
        prev = [0]*(n+1)

        for rodLength in range(n+1):
            if 1 <= rodLength:
                prev[rodLength] = price[0]*rodLength

        for i in range(1, n):
            curr = [0]*(n+1)
            for rodLength in range(0, n+1):
                notTake = prev[rodLength]
                take = float("-inf")
        
                if rodLength >= (i+1):
                    take = price[i] + curr[rodLength - (i+1)]
        
                curr[rodLength] = max(notTake, take)
            prev = curr

        return prev[n]

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.RodCutting([1, 6, 8, 9, 10, 19, 7, 20], 8))
    print(dummy.RodCutting([1, 5, 8, 9], 4))
    print(dummy.RodCutting([5, 5, 8, 9, 10, 17, 17, 20], 8))