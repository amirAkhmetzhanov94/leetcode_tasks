class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + (t * 2)


solution = Solution()
print(solution.theMaximumAchievableX(num=3, t=2))
