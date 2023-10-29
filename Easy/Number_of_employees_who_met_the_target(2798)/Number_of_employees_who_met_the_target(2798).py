class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
        return sum([1 for emp in hours if emp >= target])


solution = Solution()
print(solution.numberOfEmployeesWhoMetTarget(hours=[0,1,2,3,4], target=2))
print(solution.numberOfEmployeesWhoMetTarget(hours=[5,1,4,2,2], target=6))