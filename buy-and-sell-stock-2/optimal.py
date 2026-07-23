class Solution:
    def stockBuySell(self, arr, n):
        ahead = [0]*2

        for index in range(n-1, -1, -1):
            curr = [0]*2
            for buy in range(1, -1, -1):
                if buy:
                    profit = max(-arr[index] + ahead[0], ahead[1])
    
                else:
                    profit = max(arr[index] + ahead[1], ahead[0])

                curr[buy] = profit

            ahead = curr

        return ahead[1]

# Time complexity: O(n)
# Space complexity: O(1) 

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.stockBuySell([7, 1, 5, 3, 6, 4], 6))
    print(dummy.stockBuySell([9, 2, 6, 4, 7, 3], 6))
    print(dummy.stockBuySell([2, 3, 4, 5, 6], 5))
    print(dummy.stockBuySell([8, 6, 5, 4, 3], 5))