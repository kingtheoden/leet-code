class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def str_to_int(s):
            result = 0
            for i, char in enumerate(s):
                result += int(char) * (10 ** (len(s) - (i+1)))
            return result

        answer = str_to_int(num1) * str_to_int(num2)
        return str(answer)
            
