class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def helper(string: str, n: int, count: int):
            if n < 1:
                output.append(string)
            else:
                if count > 0:
                    helper(string + ")", n-1, count-1)
                if count < n:
                    helper(string + "(", n-1, count+1)

        helper("", 2*n, 0)
        return output
