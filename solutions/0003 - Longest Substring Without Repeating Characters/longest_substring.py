class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        biggest = 0
        current = []
        for char in s:
            if char in current:
                if len(current) > biggest:
                    biggest = len(current)
                current = self.trim(current, char)
            current.append(char)
        return max(biggest, len(current))

    def trim(self, s: list, ch: str) -> list:
        return s[s.index(ch)+1:]
