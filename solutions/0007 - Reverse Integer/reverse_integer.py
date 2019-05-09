class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        abs_flipped = int(self.trim_zero(str(abs(x)))[::-1])
        flipped = -1 * abs_flipped if negative else abs_flipped
        return 0 if flipped < -1 * 2**31 or (2**31 - 1) < flipped else flipped

    def trim_zero(self, s: str) -> str:
        if len(s) < 2 or s[0] != "0":
            return s
        return self.trim_zero(s[1:])
            
