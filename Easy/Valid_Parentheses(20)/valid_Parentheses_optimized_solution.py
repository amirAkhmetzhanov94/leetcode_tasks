class Solution:
    def isValid(self, s: str) -> bool:
        closing_brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []

        for symbol in s:
            if symbol in closing_brackets:
                if not stack or closing_brackets.get(symbol) != stack.pop():
                    return False
            else:
                stack.append(symbol)

        return not stack




solution = Solution()
s = "([{}])"
s2 = "[(])"
s3 = "[]"
s4 = "()[]{}"
s5 = "(("

print(solution.isValid(s))