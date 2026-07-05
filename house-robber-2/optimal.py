class Solution:
    def foo(self, money):
        prev2 = 0
        prev1 = money[0]
        n = len(money)

        for i in range(1, n):
            inc = money[i] + prev2
            exc = prev1
            prev2 = prev1
            prev1 = max(inc, exc)
        
        return prev1 
        
    def houseRobber(self, money):
        n = len(money)

        money1 = money[:n-1]
        money2 = money[1:]

        return max(self.foo(money1), self.foo(money2))

# Time complexity: O(n)
# Space complexity: O(n + n)

if __name__ == "__main__":
    dummy = Solution()

    print(dummy.houseRobber([1, 2, 4]))
    print(dummy.houseRobber([2, 1, 4, 9]))
