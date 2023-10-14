from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result_list = []
        for index in range(len(nums)-1):
            if not result_list:
                result_list.append(nums[index])
            result_list.append(nums[index+1]+result_list[index])


solution = Solution()
nums = [1, 1, 1, 1, 1]
solution.runningSum(nums)