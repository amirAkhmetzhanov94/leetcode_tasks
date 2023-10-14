from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [number for tup in zip(nums[:n], nums[n:]) for number in tup]


solution = Solution()
nums = [2, 5, 1, 3, 4, 7]
n = 3
solution.shuffle(nums, n)
