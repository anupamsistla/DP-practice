class Solution:
    def RodCutting(self, price, n):
        prev = [0]*(n+1)

        for N in range(0, n+1):
            prev[N] = N*price[0]
        
        for i in range(1, n):
            curr = [0]*(n+1)
            for N in range(0, n+1):
                notTake = prev[N]
                take = float("-inf")
                cuttingLen = i + 1

                if N >= cuttingLen:
                    take = price[i] + curr[N-cuttingLen]
        
                curr[N] = max(notTake, take)
            prev = curr

        return prev[n]

# Time complexity: O(n^2)
# Space complexity: O(n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.RodCutting([1, 6, 8, 9, 10, 19, 7, 20], 8))
    print(dummy.RodCutting([1, 5, 8, 9], 4))
    print(dummy.RodCutting([5, 5, 8, 9, 10, 17, 17, 20], 8))