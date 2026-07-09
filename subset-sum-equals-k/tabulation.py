class Solution:
    def isSubsetSum(self, arr, target):
        dp = [[0]*(target+1) for _ in range(len(arr))]

        for i in range(len(arr)):
            dp[i][0] = True

        dp[0][arr[0]] = True

        for i in range(1, len(arr)):
            for target in range(1, target+1):
                notTake = dp[i-1][target]
                take = False

                if target >= arr[i]:
                    take = dp[i-1][target-arr[i]]
        
                dp[i][target] = notTake or take
        return dp[len(arr)-1][target]

# Time complexity: O(n*target)
# Space complexity: O(n*target)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.isSubsetSum([1, 2, 7, 3], 6))
    print(dummy.isSubsetSum([2, 3, 5], 6))
    print(dummy.isSubsetSum([7, 54, 4, 12, 15, 5], 9))