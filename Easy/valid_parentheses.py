import re




class Solution:
    def isValid(self, s: str) -> bool:
        while True:
            s = re.sub(r'\[\]|\{\}|\(\)', '', s)
            regex = re.search(r'\[\]|\{\}|\(\)', s)
            if not s:
                return True
            elif not regex:
                return False


s = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "{[()]}"
s5 = "["
s6 = "(([]){})"
solution = Solution()
print(solution.isValid(s6))
