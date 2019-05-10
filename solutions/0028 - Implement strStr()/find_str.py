class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for x in range(len(haystack) + 1 - len(needle)):
            if haystack[x:x+len(needle)] == needle:
                return x
        return -1
