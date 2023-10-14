from math import ceil


class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                high = mid
                low = mid + 1
            else:
                high = mid - 1
        return high


solution = Solution()
x = 8
x2 = 36  # expected 6
x3 = 2  # expected 1
x4 = 5  # expected
print(solution.mySqrt(36))

# 36 = 18x2 = 9x2x2= 3x3x2x2
