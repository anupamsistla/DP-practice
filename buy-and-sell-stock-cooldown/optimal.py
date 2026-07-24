class Solution:
    def maxProfit(self, prices):
        ahead1 = [0]*2
        ahead2 = [0]*2
        n = len(prices)

        for index in range(n-1, -1, -1):
            curr = [0]*2
            for buy in range(2):
                profit = 0
        
                if buy:
                    profit = max(-prices[index] + ahead1[0], ahead1[1])
        
                else:
                    profit = max(prices[index] + ahead2[1], ahead1[0])
        
                curr[buy] = profit

            ahead2 = ahead1
            ahead1 = curr

        return ahead1[1]

# Time complexity: O(n*2)
# Space complexity: O(1)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.maxProfit([1,2,3,0,2]))
    print(dummy.maxProfit([1]))
    print(dummy.maxProfit([3,2,6,5,0,3]))
