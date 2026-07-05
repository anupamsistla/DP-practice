class Solution:
    def foo(self, money):
        prev = money[0]
        prev2 = 0
        n = len(money)

        for i in range(1, n):
            pick = prev2 + money[i]
            notPick = prev
            prev2 = prev
            prev = max(pick, notPick)
        
        return prev
        
    def houseRobber(self, money):
        n = len(money)
        temp1 = money[:n-1]
        temp2 = money[1:]

        return max(self.foo(temp1), self.foo(temp2))
    


if __name__ == "__main__":
    dummy = Solution()
    test1 = [2, 1, 4, 9, 10]

    print(dummy.houseRobber(test1))