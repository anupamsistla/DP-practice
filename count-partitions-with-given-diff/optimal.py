class Solution:   
    def countPartitions(self, n, diff, arr):
        totalSum = sum(arr)

        prev = [0]*(totalSum+1)

        prev[0] = 1
        
        prev[arr[0]] = 1

        for i in range(1, len(arr)):
            curr = [0]*(totalSum+1)
            curr[0] = 1
            for target in range(1, totalSum+1):
                notTake = prev[target]
                take = 0

                if target >= arr[i]:
                    take = prev[target - arr[i]]
                
                curr[target] = take + notTake
            prev = curr

        count = 0
        for i in range(totalSum // 2 + 1):
            if curr[i] != 0:
                absDiff = abs(totalSum - i - i)
                
                if absDiff == diff:
                    count += curr[i]

        return count

# Time complexity: O(n * totalSum)
# Space complexity: O(n)
    
if __name__ == "__main__":
    dummy = Solution()
    print(dummy.countPartitions(4, 1, [1, 1, 2, 3]))
    print(dummy.countPartitions(4, 2, [1, 2, 3, 4]))
    print(dummy.countPartitions(4, 3, [5, 2, 6, 4]))
                    


      