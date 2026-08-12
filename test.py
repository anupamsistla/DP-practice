from typing import List
class Solution:
    def canPartition(self, arr: List[int]) -> bool:
        target = sum(arr)
        dp = [[False]*(target+1) for _ in range(len(arr))]

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

        n = len(arr)
        for t in range(0, target+1 // 2):
            check = target - t

            if check == t and dp[n-1][check] == True and dp[n-1][t] == True:
                return True

        return False

# last row represents the sums we can form using all elements of the array

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.canPartition([1, 2, 7, 3]))
    print(dummy.canPartition([2, 3, 5]))
    print(dummy.canPartition([7, 54, 4, 12, 15, 5]))