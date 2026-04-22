class Solution:
    def isPalindrome(self, x: str) -> bool:
        return x == x[::-1]

    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            for j in range(i+1,len(s) + 1):
                if self.isPalindrome(s[i:j]) and len(s[i:j]) > len(longest):
                    longest = s[i:j]
        return longest