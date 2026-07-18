class Solution:
    def minInsertion(self, s):
        n = m = len(s)
        prev = [0]*(m+1)

        str1 = s
        str2 = s[::-1]

        for i in range(1, n+1):
            curr = [0]*(m+1)
            for j in range(1, m+1):
                if str1[i-1] == str2[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev = curr

        return m - prev[m]
    
# Time complexity: O(m*n)
# Space complexity: O(m)

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.minInsertion("abcaa"))
    print(dummy.minInsertion("codingninjas"))
    print(dummy.minInsertion("ba"))
