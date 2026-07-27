class Solution:
    def LongestBitonicSequence(self, arr):
        n = len(arr)
        dp1 = [1]*n

        for i in range(n):
            for j in range(i):
                if arr[i] > arr[j] and 1 + dp1[j] > dp1[i]:
                    dp1[i] = 1 + dp1[j]

        dp2 = [1]*n

        for i in range(n-1, -1, -1):
            for j in range(n-1, i, -1):
                if arr[i] > arr[j] and 1 + dp2[j] > dp2[i]:
                    dp2[i] = 1 + dp2[j]

        maxI = 1
        for i in range(n):
            maxI = max(maxI, dp1[i] + dp2[i] - 1)
        return maxI

# Time complexity: O(n^2)
# Space complexity: O(n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.LongestBitonicSequence([5, 1, 4, 2, 3, 6, 8, 7]))
    print(dummy.LongestBitonicSequence([10, 20, 30, 40, 50, 40, 30, 20]))
    print(dummy.LongestBitonicSequence([12, 11, 10, 15, 18, 17, 16, 14]))
    print(dummy.LongestBitonicSequence([1, 11, 2, 10, 4, 5, 2, 1]))