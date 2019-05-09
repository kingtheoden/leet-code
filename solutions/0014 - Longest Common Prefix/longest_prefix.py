class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1:
            return ""
        result = self.helper(strs[0], strs[1:])
        return ''.join(result)

    def helper(self, test: str, words: List[str]) -> List[str]:
        result = []
        for i, ch in enumerate(test):
            for word in words:
                if len(word) - 1 < i or word[i] != ch:
                    return result
            result.append(ch)
        return result
