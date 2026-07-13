class Solution:
    def perfectSum(self, arr, K):
        prev = [0]*(K+1)
        
        prev[0] = 1
        
        prev[arr[0]] = 1

        for i in range(1, len(arr)):
            curr = [0]*(K+1)
            curr[0] = 1
            for k in range(1, K+1):
                notTake = prev[k]
                take = 0

                if k >= arr[i]:
                    take = prev[k - arr[i]]
        
                curr[k] = notTake + take
            prev = curr

        return prev[K]
    
# Time complexity: O(n*K)
# Space complexity: O(n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.perfectSum([1, 1, 2, 3, 4], 7))
    print(dummy.perfectSum([4, 4, 8], 8))
    print(dummy.perfectSum([1, 2, 2, 3], 3))
    print(dummy.perfectSum([4, 3, 7], 7))