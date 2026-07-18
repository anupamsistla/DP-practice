class Solution:
    def minOperations(self, str1, str2):
        n, m = len(str1), len(str2)
        prev = [0]*(m+1)

        for i in range(1, n+1):
            curr = [0]*(m+1)
            for j in range(1, m+1):
                if str1[i-1] == str2[j-1]:
                    curr[j] = 1 + prev[j-1]
                
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev = curr

        lcs = prev[m]
        leftDel = n - lcs
        rightAdd = m - lcs
        
        return leftDel + rightAdd

# Time complexity: O(m*n)
# Space complexity: O(m)
        
if __name__ == "__main__":
    dummy = Solution()
    print(dummy.minOperations("kitten", "sitting"))
    print(dummy.minOperations("flaw", "lawn"))
    print(dummy.minOperations("abcdef","ghijkl"))