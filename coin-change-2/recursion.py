class Solution:
    def foo(self, index, amount, coins):
        if index == 0:
            if amount % coins[0] == 0:
                return 1
            else:
                return 0

        notTake = self.foo(index-1, amount, coins)
        take = 0

        if amount >= coins[index]:
            take = self.foo(index, amount - coins[index], coins)
        return notTake + take   

    def count(self, coins, N, amount):
        return self.foo(N-1, amount, coins)
    
# Time complexity: O(2^amount/w) 
# Space complexity: O(n + amount/w)
# Where 'w' is the smallest denomination in coins

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.count([1,2,3], 3, 4))
    print(dummy.count([2,4,10], 3, 10))
    print(dummy.count([3,5,7,10], 4, 11))
    print(dummy.count([3,5,7], 3, 4))

       