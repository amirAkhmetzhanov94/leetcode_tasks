class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        multiply_result = 1
        for number in [int(number) for number in str(n)]:
            multiply_result *= number
        return multiply_result - sum([int(number) for number in str(n)])


solution = Solution()
n = 4421
print(solution.subtractProductAndSum(n))
