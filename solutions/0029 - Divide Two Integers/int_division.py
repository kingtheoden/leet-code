class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        accume = 0

        for i, ch in enumerate(str(dividend)):
            accume += int(ch)
            stage = 0
            while accume >= divisor:
                accume -= divisor
                stage += 1
            accume = int(str(accume) + "0") if accume > 0 else accume
            stage = str(stage)
            for _ in range(len(str(dividend)) - (i + 1)):
                stage += "0"
            result += int(stage)

        return min(result, 2147483647) if positive else max(-result, -2147483648)
