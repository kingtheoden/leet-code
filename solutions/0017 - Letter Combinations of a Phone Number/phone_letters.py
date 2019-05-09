class Solution:
    dic = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        def helper(digits, combo):
            if len(digits) < 1:
                result.append(combo)
                return
            for letter in self.dic[digits[0]]:
                helper(digits[1:], combo + letter)
        if digits:
            helper(digits, "")
        return result
        
