class Solution:
    def intToRoman(self, num: int) -> str:
        if num < 4:
            return num * "I"
        elif num < 5:
            return "IV"
        elif num < 9:
            return "V" + self.intToRoman(num - 5)
        elif num < 10:
            return "IX"
        elif num < 40:
            return (num // 10) * "X" + self.intToRoman(num % 10)
        elif num < 50:
            return "XL" + self.intToRoman(num - 40)
        elif num < 90:
            return "L" + self.intToRoman(num - 50)
        elif num < 100:
            return "XC" + self.intToRoman(num - 90)
        elif num < 400:
            return (num // 100) * "C" + self.intToRoman(num % 100)
        elif num < 500:
            return "CD" + self.intToRoman(num - 400)
        elif num < 900:
            return "D" + self.intToRoman(num - 500)
        elif num < 1000:
            return "CM" + self.intToRoman(num - 900)
        elif num < 4000:
            return "M" * (num // 1000) + self.intToRoman(num % 1000)
