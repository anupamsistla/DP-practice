class Solution:
    def compareWords(self, word1, word2):
        if len(word1) != len(word2) + 1:
            return False

        first = second = 0

        while first < len(word1):
            if second < len(word2) and word1[first] == word2[second]:
                first += 1
                second += 1

            else:
                first += 1

        return first == len(word1) and second == len(word2)

    def longestStringChain(self, words):
        words = sorted(words, key=len)
        dp = [1]*len(words)
        maxI = 1

        for i in range(len(words)):
            for j in range(i):
                if self.compareWords(words[i], words[j]) and 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
            maxI = max(maxI, dp[i])
        return maxI

# Time complexity: O(n^2 * m)
# Space complexity: O(n)

# Note: m is the length of the longest word

if __name__ == "__main__":
    dummy = Solution()
    print(dummy.longestStringChain(["a", "ab", "abc", "abcd", "abcde"]))
    print(dummy.longestStringChain(["dog", "dogs", "dots", "dot", "d", "do"]))
    print(dummy.longestStringChain(["a", "aa", "aaa", "aaaa", "b", "bb", "bbb"]))
    print(dummy.longestStringChain(["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"]))