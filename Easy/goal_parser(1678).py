class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("(al)", "al").replace("()", "o")


solution = Solution()
command = "(al)G(al)()()G"

print(solution.interpret(command))