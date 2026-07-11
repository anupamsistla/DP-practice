class Solution:   
    def countPartitions(self, n, diff, arr):
        totalSum = sum(arr)

        dp = [[0]*(totalSum+1) for _ in range(len(arr))]

        for i in range(len(arr)):
            dp[i][0] = 1
        
        dp[0][arr[0]] = 1

        for i in range(1, len(arr)):
            for target in range(1, totalSum+1):
                notTake = dp[i-1][target]
                take = 0

                if target >= arr[i]:
                    take = dp[i-1][target - arr[i]]
                
                dp[i][target] = take + notTake

        count = 0
        for i in range(totalSum // 2 + 1):
            if dp[n-1][i] != 0:
                absDiff = abs(totalSum - i - i)
                
                if absDiff == diff:
                    count += dp[n-1][i]

        return count

# Time complexity: O(n * totalSum)
# Space complexity: O(n * totalSum)
    
if __name__ == "__main__":
    dummy = Solution()
    print(dummy.countPartitions(4, 1, [1, 1, 2, 3]))
    print(dummy.countPartitions(4, 2, [1, 2, 3, 4]))
    print(dummy.countPartitions(4, 3, [5, 2, 6, 4]))
                    


      