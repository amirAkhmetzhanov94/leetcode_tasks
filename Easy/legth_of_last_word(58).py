class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

solution = Solution()
s = "Hello World"
s2 = "   fly me   to   the moon  "
print(solution.lengthOfLastWord(s))