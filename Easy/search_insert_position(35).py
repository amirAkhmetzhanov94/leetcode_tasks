from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            index = 0
            while index < len(nums):
                if nums[index] > target:
                    return index
                elif nums[index] < target:
                    index += 1
            return index

solution = Solution()
nums = [1, 3, 5, 6]
nums2 = [2, 3, 4, 8, 10]
target = 7
target2 = 0
print(solution.searchInsert(nums, target))
