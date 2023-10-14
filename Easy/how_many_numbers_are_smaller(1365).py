from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        iter_count = 0
        while iter_count < len(nums):
            count = 0
            difference_number = nums.pop(0)
            for number in nums:
                if number < difference_number:
                    count += 1
            result.append(count)
            nums.append(difference_number)
            iter_count += 1
        return result

solution = Solution()
nums = [8,1,2,2,3]
print(solution.smallerNumbersThanCurrent(nums))