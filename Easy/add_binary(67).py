class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0" and b == "0":
            return "0"
        total_number = 0
        for string in [a, b]:
            counter = 0
            for number in string[::-1]:
                total_number += int(number) * (2 ** counter)
                counter += 1
        result = []
        while total_number != 0:
            result.append(str((int(total_number % 2))))
            total_number //= 2
        return "".join(result[::-1])


solution = Solution()
a = "11"
b = "1"
print(solution.addBinary(a, b))
