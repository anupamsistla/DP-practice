class Solution:
    def foo(self, index, arr, K):
        if K == 0:
            return 1
        
        if index == 0:
            return arr[0] == K
    
        notTake = self.foo(index-1, arr, K)
        take = 0

        if K >= arr[index]:
            take = self.foo(index-1, arr, K - arr[index])
        
        return notTake + take

    def perfectSum(self, arr, K):
        return self.foo(len(arr)-1, arr, K)
    
# Time complexity: O(2^n)
# Space complexity: O(n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.perfectSum([1, 1, 2, 3, 4], 7))
    print(dummy.perfectSum([4, 4, 8], 8))
    print(dummy.perfectSum([1, 2, 2, 3], 3))
    print(dummy.perfectSum([4, 3, 7], 7))