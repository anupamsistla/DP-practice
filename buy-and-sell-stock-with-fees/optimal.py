class Solution:
    def stockBuySell(self, arr, n, fee):
        ahead = [0]*2 

        for index in range(n-1, -1, -1):
            curr = [0]*2 
            for buy in range(2):
                profit = 0
                
                if buy: 
                    profit = max(-arr[index] + ahead[0], ahead[1])
        
                else:
                    profit = max(arr[index] + ahead[1] - fee, ahead[0])
        
                curr[buy] = profit
            ahead = curr

        return ahead[1]

# Time complexity: O(n*2)
# Space complexity: O(1)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.stockBuySell([1, 3, 4, 0, 2], 5, 1))
    print(dummy.stockBuySell([1, 3, 2, 8, 4, 9], 6, 2))
    print(dummy.stockBuySell([10, 3, 7, 5, 1, 3], 6, 3))
