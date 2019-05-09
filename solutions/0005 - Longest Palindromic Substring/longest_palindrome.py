class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        biggest = s[0]
        for L in range(len(s) - 1):
            for R in range(L + 2, len(s) + 1):
                new_sub = s[L:R]
                if len(new_sub) > len(biggest) and self.is_pal(new_sub):
                    biggest = new_sub
        return biggest

    def is_pal(self, s: str) -> bool:
        if len(s) % 2 == 0:
            return s[:len(s) // 2] == s[len(s) // 2:][::-1]
        else:
            return s[:len(s) // 2] == s[(len(s) // 2) + 1:][::-1]
