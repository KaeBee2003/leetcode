class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = ""
        for i in range(len(strs[0])):
            for word in strs:
                if len(word) <= i or word[i] != strs[0][i]:
                    return a
            a = a + word[i]
        return a
            