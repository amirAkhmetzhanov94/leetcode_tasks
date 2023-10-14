from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0:
            for _ in nums1:
                nums1.pop()
        if n == 0:
            for _ in nums2:
                nums2.pop()
        for number in nums1[m:]:
            nums1.remove(number)
        for number in nums2[n:]:
            nums2.remove(number)
        nums1 += nums2
        nums1.sort()
        return




solution = Solution()
nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3

print(solution.merge(nums1, m, nums2, n))
