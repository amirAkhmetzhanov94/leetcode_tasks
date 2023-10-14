class Solution:
    def isPalindrome(self, x: int) -> bool:
        numbers_1 = [number for number in str(x)]
        numbers_copy = numbers_1.copy()
        numbers_1.reverse()
        if numbers_1 == numbers_copy:
            return True


ts_1 = 121
ts_2 = -121
ts_3 = 10
solution = Solution()
print(solution.isPalindrome(ts_3))
