class Solution:        
    def stockBuySell(self, arr, n):
        ahead = [[0]*3 for _ in range(2)]

        for index in range(n-1, -1, -1):
            curr = [[0]*3 for _ in range(2)]
            for buy in range(2):
                for cap in range(1, 3):
                    profit = 0
                    
                    if buy:
                        profit = max(-arr[index] + ahead[0][cap], ahead[1][cap])
            
                    else:
                        profit = max(arr[index] + ahead[1][cap-1], ahead[0][cap])

                    curr[buy][cap] = profit

            ahead = curr
            
        return ahead[1][2]
    
# Time complexity: O(n*2*3) = O(n)
# Space complexity: O(2*3) = O(1)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.stockBuySell([4, 2, 7, 1, 11, 5], 6))
    print(dummy.stockBuySell([1, 3, 2, 8, 4, 9], 6))
    print(dummy.stockBuySell([5, 7, 2, 10, 6, 9], 6))
    print(dummy.stockBuySell([3, 3, 5, 0, 0, 3, 1, 4], 8))