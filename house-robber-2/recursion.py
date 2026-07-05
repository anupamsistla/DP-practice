class Solution:
    def foo(self, index, money):
        if index < 0:
            return 0

        inc = money[index] + self.foo(index-2, money)
        exc = self.foo(index-1, money)
        return max(inc, exc)
        
    def houseRobber(self, money):
        n = len(money)

        money1 = money[:n-1]
        money2 = money[1:]

        return max(self.foo(n-2, money1), self.foo(n-2, money2))

# Time complexity: O(2^n+1)
# Space complexity: O(n + n + n)

if __name__ == "__main__":
    dummy = Solution()

    print(dummy.houseRobber([1, 2, 4]))
    print(dummy.houseRobber([2, 1, 4, 9]))
