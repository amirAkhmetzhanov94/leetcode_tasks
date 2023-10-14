from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_number = max(candies)
        result = []
        for kid_has in candies:
            if (kid_has+extraCandies) >= max_number:
                result.append(True)
            else:
                result.append(False)
        return result

solution = Solution()
candies = [2,3,5,1,3]
extraCandies = 3
print(solution.kidsWithCandies(candies, extraCandies))