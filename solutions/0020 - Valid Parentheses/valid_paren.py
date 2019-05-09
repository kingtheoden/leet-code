class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')': '(', '}': '{', ']': '['}
        stack = []
        for ch in s:
            if ch in dic:
                if not stack or stack.pop() != dic[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack
