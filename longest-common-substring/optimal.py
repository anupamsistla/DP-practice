class Solution:
    def lcs(self, str1, str2):
        n, m = len(str1), len(str2)
        prev = [0]*(m+1)
        toRet = 0

        for i in range(1, n+1):
            curr = [0]*(m+1)
            for j in range(1, m+1):
                if str1[i-1] == str2[j-1]:
                    curr[j] = 1 + prev[j-1]
                    toRet = max(toRet, curr[j])
                else:
                    curr[j] = 0
            prev = curr
        return toRet

# Time complexity: O(m*n)
# Space complexity: O(m)
        
if __name__ == "__main__":
    dummy = Solution()
    print(dummy.lcs("bdefg", "bfg"))
    print(dummy.lcs("mnop", "mnq"))
    print(dummy.lcs("abc","dafb"))
    print(dummy.lcs("acd", "ced"))