from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        for number in nums[index+1:]:
            if number == nums[index]:
                nums.pop(nums.index(number))
                index -= 1
            index += 1
        return index + 1

solution = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(solution.removeDuplicates(nums))
