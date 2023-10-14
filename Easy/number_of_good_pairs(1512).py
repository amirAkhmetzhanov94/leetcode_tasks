from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        index, count = 0, 0
        while index < len(nums):
            for number in nums[index+1:]:
                if nums[index] == number:
                    count +=1
            index +=1
        return count


solution = Solution()
nums = [1,2,3]
nums2 = [1,2,3,1,1,3]
solution.numIdenticalPairs(nums2)