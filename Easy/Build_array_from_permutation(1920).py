from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[index] for index in nums]


solution = Solution()
nums = [0, 2, 1, 5, 3, 4]
print(solution.buildArray(nums))