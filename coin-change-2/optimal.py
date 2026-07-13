class Solution:
    def count(self, coins, N, amount):
        prev = [0]*(amount + 1)

        for a in range(amount + 1):
            if a % coins[0] == 0:
                prev[a] = 1
        
        for i in range(1, len(coins)):
            curr = [0]*(amount + 1)
            for a in range(amount + 1):
                notTake = prev[a]
                take = 0

                if a >= coins[i]:
                    take = curr[a - coins[i]]
        
                curr[a] = notTake + take
            prev = curr

        return prev[amount]
    
# Time complexity: O(n * amount) 
# Space complexity: O(a)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.count([1,2,3], 3, 4))
    print(dummy.count([2,4,10], 3, 10))
    print(dummy.count([3,5,7,10], 4, 11))
    print(dummy.count([3,5,7], 3, 4))
