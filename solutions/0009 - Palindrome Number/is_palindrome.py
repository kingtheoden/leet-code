class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        for i, ch in enumerate(string[:len(string) + 1]):
            if ch != string[len(string)- 1 - i]:
                return False
        return True
