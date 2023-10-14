from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [number for number in str(int("".join(map(str, digits))) + 1)]

solution = Solution()
digits = [1,2,3]
solution.plusOne(digits)