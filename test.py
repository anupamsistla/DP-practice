class Solution:
    def foo(self, index, arr, target, dp):
        if dp[index][target] != -1:
            return dp[index][target]
        
        if index == 0:
            if target == arr[index]:
                return True

            else:
                return False

        if target == 0:
            return True

        notTake = self.foo(index-1, arr, target, dp)
        take = False
        if target > 0 and arr[index] <= target:
            take = self.foo(index-1, arr, target - arr[index], dp)

        dp[index][target] = notTake or take
        return dp[index][target]

    def isSubsetSum(self, arr, target):
        n = len(arr)
        prev = [False] * (target+1)

        for t in range(target + 1):
            if t == arr[0]:
                prev[t] = True


        for i in range(1, n):
            curr = [False] * (target+1)
            for t in range(target + 1):
                if t == 0:
                    curr[t] =  True

                else:
                    notTake = prev[t]
                    take = False
                    if t > 0 and arr[i] <= t:
                        take = prev[t - arr[i]]
            
                    curr[t] = notTake or take
            prev = curr
        return prev[target]



if __name__ == "__main__":
    dummy = Solution()
    print(dummy.isSubsetSum([1, 2, 7, 3], 6))
    print(dummy.isSubsetSum([2, 3, 5], 6))
    print(dummy.isSubsetSum([7, 54, 4, 12, 15, 5], 9))