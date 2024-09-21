from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left_pointer = 0
        for number in nums:
            if number != nums[left_pointer]:
                nums[nums.index(number)] = nums[left_pointer]
                left_pointer += 1
                nums[left_pointer] = number
        return left_pointer + 1


solution = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums2 = [1, 1, 2]

