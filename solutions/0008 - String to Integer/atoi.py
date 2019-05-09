class Solution:
    def myAtoi(self, s: str) -> int:
        num_s = self.trim(s)
        if len(num_s) < 1 or num_s == "-" or num_s == "+":
            return 0
        if num_s[0] == "+":
            num_s = num_s[1:]
        num = int(num_s)
        if num > (2**31 - 1):
            num = 2**31 - 1
        elif num < (-2**31):
            num = -2**31
        return num

    def trim(self, s: str) -> str:
        result = []
        activate = False
        for ch in s:
            if activate:
                if ch.isdigit():
                    result.append(ch)
                else:
                    return ''.join(result)
            else:
                if ch.isdigit() or ch == "-" or ch == "+":
                    result.append(ch)
                    activate = True
                elif ch.isspace():
                    continue
                else:
                    return ''
        return ''.join(result)
