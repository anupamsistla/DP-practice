class Solution:
    def targetSum(self, n, target, arr):
        totalSum = 0
        
        for num in arr:
            totalSum += num 
        
        prev = [0]*(totalSum + 1)

        for t in range(totalSum + 1):
            if arr[0] == 0 and t == 0:
                prev[t] = 2
            
            elif arr[0] == t or t == 0:
                prev[t] = 1
        
        for i in range(1, n):
            curr = [0]*(totalSum + 1)
            for t in range(totalSum + 1):
                notTake = prev[t]
                take = 0

                if t >= arr[i]:
                    take = prev[t - arr[i]]
        
                curr[t] = notTake + take
            prev = curr

        count = 0

        for i in range(totalSum + 1):
            currDiff = totalSum - i - i

            if currDiff == target and prev[i] != 0:
                count += prev[i]
        return count

# Time complexity: O(n * totalSum)
# Space complexity: O(n * totalSum)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.targetSum(5, 1, [0, 1, 1, 2, 3]))
    print(dummy.targetSum(4, 1, [0, 0, 0, 1]))
    print(dummy.targetSum(2, 1, [1, 0]))
    print(dummy.targetSum(2, 0, [1, 1]))

      