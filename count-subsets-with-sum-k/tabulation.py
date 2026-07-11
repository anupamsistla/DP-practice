class Solution:
    def perfectSum(self, arr, K):
        dp = [[0]*(K+1) for _ in range(len(arr))]
        
        for i in range(len(arr)):
            dp[i][0] = 1
        
        dp[0][arr[0]] = 1

        for i in range(1, len(arr)):
            for k in range(1, K+1):
                notTake = dp[i-1][k]
                take = 0

                if K >= arr[i]:
                    take = dp[i-1][k - arr[i]]
        
                dp[i][k] = notTake + take

        return dp[len(arr)-1][K]
    
# Time complexity: O(n*K)
# Space complexity: O(n*K)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.perfectSum([1, 1, 2, 3, 4], 7))
    print(dummy.perfectSum([4, 4, 8], 8))
    print(dummy.perfectSum([1, 2, 2, 3], 3))
    print(dummy.perfectSum([4, 3, 7], 7))