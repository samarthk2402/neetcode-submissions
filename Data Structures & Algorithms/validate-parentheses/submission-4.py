class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(': ')',
            '{': '}',
            '[': ']'}

        bracket_stack = []

        for char in s:

            if char in brackets.keys():
                bracket_stack.append(char)
            elif char in brackets.values():
                if len(bracket_stack) > 0:
                    if char == brackets[bracket_stack[-1]]:
                        bracket_stack.pop()
                    else:
                        return False
                else:
                    return False

        if len(bracket_stack) > 0:
            return False
        else:
            return True