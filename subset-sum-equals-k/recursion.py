class Solution:
    def foo(self, index, target, arr):
        if target == 0:
            return True
    
        if index == 0:
            return arr[0] == target
        
        notTake = self.foo(index-1, target, arr)
        take = False

        if target >= arr[index]:
            take = self.foo(index-1, target-arr[index], arr)
        
        return notTake or take
        
    def isSubsetSum(self, arr, target):
        return self.foo(len(arr)-1, target, arr)

# Time complexity: O(2^n)
# Space complexity: O(n)
        

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.isSubsetSum([1, 2, 7, 3], 6))
    print(dummy.isSubsetSum([2, 3, 5], 6))
    print(dummy.isSubsetSum([7, 54, 4, 12, 15, 5], 9))