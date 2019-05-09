class Solution:

    dic = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90,
          "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}

    def romanToInt(self, s: str) -> int:
        if len(s) < 1:
            return 0
        if len(s) == 1:
            return self.dic[s]
        else:
            if s[:2] in self.dic.keys():
                return self.dic[s[:2]] + self.romanToInt(s[2:])
            else:
                return self.dic[s[0]] + self.romanToInt(s[1:])
        
