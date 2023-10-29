class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        while True:
            if n % 2 == 0 and n % n == 0:
                return n
            n *= 2


solution = Solution()
print(solution.smallestEvenMultiple(6))