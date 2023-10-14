from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for value,index in zip(nums,index):
            target.insert(index, value)
        return target

solution = Solution()
nums = [0,1,2,3,4]
index = [0,1,2,2,1]
solution.createTargetArray(nums, index)