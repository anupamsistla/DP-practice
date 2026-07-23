class Solution:
    def stockBuySell(self, arr, n, k):
        ahead = [0]*(2*k+1)

        for index in range(n-1, -1, -1):
            curr = [0]*(2*k+1)
            for K in range(1, 2*k+1):
                profit = 0
                
                if K % 2 == 0:
                    profit = max(-arr[index] + ahead[K-1], ahead[K])
        
                else:
                    profit = max(arr[index] + ahead[K-1], ahead[K])
        
                curr[K] = profit
            ahead = curr
        
        return curr[2*k]

# Time complexity: O(n*k)
# Space complexity: O(k)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.stockBuySell([4, 2, 7, 1, 11, 5], 6, 2))
    print(dummy.stockBuySell([1, 3, 2, 8, 4, 9], 6, 3))
    print(dummy.stockBuySell([5, 7, 2, 10, 6, 9], 6, 1))
    print(dummy.stockBuySell([3, 3, 5, 0, 0, 3, 1, 4], 8, 3))