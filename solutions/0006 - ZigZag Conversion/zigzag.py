class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        if numRows == 2:
            return s[::2] + s[1::2]
        result = [[] for x in range(numRows)]
        row = 0
        inc = 1
        for ch in s:
            result[row].append(ch)
            if row == 0:
                inc = 1
            elif row == numRows - 1:
                inc = -1
            row += inc
        return ''.join([''.join(li) for li in result])
