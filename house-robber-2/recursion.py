class Solution:
    def foo(self, index, money):
        if index == 0:
            return money[index]
        if index < 0:
            return 0
    
        pick = self.foo(index-2, money) + money[index]
        notPick = self.foo(index-1, money)
    
        return max(pick, notPick)

    def houseRobber(self, money):
        n = len(money)
        temp1 = money[:n-1]
        temp2 = money[1:]
        print(temp1)
        print(temp2)

        return max(self.foo(n-2, temp1), self.foo(n-2, temp2))
    


if __name__ == "__main__":
    dummy = Solution()
    test1 = [2, 1, 4, 9, 10]

    print(dummy.houseRobber(test1))