from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


solution = Solution()
nums = [3,2,2,3]
nums_2 = [0,1,2,2,3,0,4,2]
val = 2
print(solution.removeElement(nums_2, val))
print(nums_2)