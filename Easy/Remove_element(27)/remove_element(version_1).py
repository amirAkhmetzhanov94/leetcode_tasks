from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = 0
        for index in range(len(nums)):
            if nums[index] < val or nums[index] > val:
                nums[length] = nums[index]
                length += 1
        return length


solution = Solution()
nums = [3,2,2,3]
val = 3
print(solution.removeElement(nums, val))