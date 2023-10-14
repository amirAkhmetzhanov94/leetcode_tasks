from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = ['0' for _ in range(len(indices))]
        for letter, index in zip(s, indices):
            result[index] = letter
        return ''.join(result)

solution = Solution()
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(solution.restoreString(s, indices))