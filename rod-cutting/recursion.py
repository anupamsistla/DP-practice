class Solution:
    def foo(self, index, n, price):
        if index == 0:
            return n*price[0]
        
        notTake = self.foo(index-1, n, price)
        take = float("-inf")
        cuttingLen = index + 1

        if n >= cuttingLen:
            take = price[index] + self.foo(index, n-cuttingLen, price)
        
        return max(notTake, take)
    
    def RodCutting(self, price, n):
        return self.foo(n-1, n, price)

# Time complexity: O(2^n) [Exponential]
# Space complexity: O(n)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.RodCutting([1, 6, 8, 9, 10, 19, 7, 20], 8))
    print(dummy.RodCutting([1, 5, 8, 9], 4))
    print(dummy.RodCutting([5, 5, 8, 9, 10, 17, 17, 20], 8))