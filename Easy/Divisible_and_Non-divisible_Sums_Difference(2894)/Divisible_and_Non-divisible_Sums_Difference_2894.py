class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        list_of_not_divisible = [
            number
            for number in range(1, n + 1)
            if number % m != 0
        ]
        list_of_divisible = [
            number
            for number in range(1, n + 1)
            if number % m == 0
        ]
        return sum(list_of_not_divisible) - sum(list_of_divisible)


solution = Solution()
print(solution.differenceOfSums(n=5, m=6))
print(solution.differenceOfSums(n=10, m=3))
