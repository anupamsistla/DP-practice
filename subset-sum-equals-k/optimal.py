class Solution:
    def foo(self, index, target, arr, dp):
        if target == 0:
            return True
        
        if dp[index][target] != -1:
            return dp[index][target]
    
        if index == 0:
            return arr[0] == target
        
        notTake = self.foo(index-1, target, arr, dp)
        take = False

        if target >= arr[index]:
            take = self.foo(index-1, target-arr[index], arr, dp)
        
        dp[index][target] = notTake or take
        return dp[index][target]
        
    def isSubsetSum(self, arr, target):
        dp = [[-1]*(target+1) for _ in range(len(arr))]
        return self.foo(len(arr)-1, target, arr, dp)

# Time complexity: O(n*target)
# Space complexity: O(n*target + n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.isSubsetSum([1, 2, 7, 3], 6))
    print(dummy.isSubsetSum([2, 3, 5], 6))
    print(dummy.isSubsetSum([7, 54, 4, 12, 15, 5], 9))