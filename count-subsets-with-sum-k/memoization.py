class Solution:
    def foo(self, index, arr, K, dp):
        if K == 0:
            return 1
        
        if dp[index][K] != -1:
            return dp[index][K]

        if index == 0:
            return arr[0] == K # returns 1 if arr[0] == K else 0
    
        notTake = self.foo(index-1, arr, K, dp)
        take = 0

        if K >= arr[index]:
            take = self.foo(index-1, arr, K - arr[index], dp)
        
        dp[index][K] = notTake + take
        return dp[index][K]

    def perfectSum(self, arr, K):
        dp = [[-1]*(K+1) for _ in range(len(arr))]
        return self.foo(len(arr)-1, arr, K, dp)
    
# Time complexity: O(n*K)
# Space complexity: O(n*K + n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.perfectSum([1, 1, 2, 3, 4], 7))
    print(dummy.perfectSum([4, 4, 8], 8))
    print(dummy.perfectSum([1, 2, 2, 3], 3))
    print(dummy.perfectSum([4, 3, 7], 7))