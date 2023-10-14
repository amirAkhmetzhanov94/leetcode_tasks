import string
from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        first_column, last_column = s.split(':')
        first_letter, min_value = (i for i in first_column)
        second_letter, max_value = (i for i in last_column)
        range_of_letters = list(
            string.ascii_uppercase[string.ascii_uppercase.index(first_letter):
                                   string.ascii_uppercase.index(second_letter)
                                   + 1])
        result = []
        for letter in range_of_letters:
            if int(max_value) < 2:
                result.append(''.join(letter+str(max_value)))
                continue
            for number in range(int(min_value), int(max_value)+ 1):
                result.append(''.join(letter + str(number)))
        return result


solution = Solution()
s = "U7:X9"
solution.cellsInRange(s)
