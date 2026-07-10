class Solution:
    def isSubsetSum(self, arr, target):
        curr = [False]*(target+1)
        curr[0] = True
        
        curr[arr[0]] = True

        for i in range(1, len(arr)):
            temp = [False]*(target+1)
            temp[0] = True
            for target in range(1, target+1):
                notTake = curr[target]
                take = False

                if target >= arr[i]:
                    take = curr[target-arr[i]]
        
                temp[target] = notTake or take
            curr = temp

        return curr[target]

# Time complexity: O(n*target)
# Space complexity: O(target)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.isSubsetSum([1, 2, 7, 3], 6))
    print(dummy.isSubsetSum([2, 3, 5], 6))
    print(dummy.isSubsetSum([7, 54, 4, 12, 15, 5], 9))