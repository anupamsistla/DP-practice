class Solution:
    def editDistance(self, start, target):
        n, m = len(start), len(target)
        prev = [0]*(m+1)
        
        for j in range(m+1):
            prev[j] = j

        prev[0] = 0

        for i in range(1, n+1):
            curr = [0]*(m+1)
            curr[0] = i
            for j in range(1, m+1):
                if start[i-1] == target[j-1]:
                    curr[j] = prev[j-1]

                else:
                    insert = 1 + curr[j-1]
                    delete = 1 + prev[j]
                    replace = 1 + prev[j-1]

                    curr[j] = min(insert, delete, replace)
            prev = curr
        
        return prev[m]
    
# Time complexity: O(n*m)
# Space complexity: O(m)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.editDistance("horse", "ros"))
    print(dummy.editDistance("intention", "execution"))
    print(dummy.editDistance("abcdefg", "azced"))