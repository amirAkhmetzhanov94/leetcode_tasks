from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for operation in operations:
            if operation in ["--X", "X--"]:
                x -= 1
            elif operation in ["++X", "X++"]:
                x += 1
        return x



solution = Solution()
operations = ["--X","X++","X++"]
solution.finalValueAfterOperations(operations)