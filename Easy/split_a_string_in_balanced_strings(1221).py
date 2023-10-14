class Solution:
    def balancedStringSplit(self, s: str) -> int:
        counter = 0
        result = 0
        for letter in s:
            if letter == "L":
                counter += 1
            elif letter == "R":
                counter -= 1
            if counter == 0:
                result += 1
        return result

solution = Solution()
s = "LLLLRRRR"
print(solution.balancedStringSplit(s))