class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        for i, ch in enumerate(s):
            # if the char is and open paren, push it to the stack.
            if ch == '(':
                stack.append(i)
            # if the char is a close paren, pop an adjacent open paren
            # on the stack or add the close paren to the stack indicating
            # an invalid char
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)

        # The stack is now populated with the indicies of invalid chars
        # The correct result is the largest space between those indicies.

        if not stack:
            # if the stack is empty, the whole string is valid
            return len(s)

        longest = 0

        # Starting at the end of the string
        b = len(s)
        while stack:
        # checking the spaces in between indices
            a = stack.pop()
            longest = max(longest, b - a - 1)
            b = a

        # Checking the space between the beginning of the string
        # and the earliest index.
        longest = max(longest, a)

        return longest

        
