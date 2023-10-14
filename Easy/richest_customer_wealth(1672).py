from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        results = []
        for account in accounts:
            count = 0
            for number in account:
                count += number
            results.append(count)
        return max(results)

solution = Solution()
accounts = [[1,2,3],[3,2,1]]
print(solution.maximumWealth(accounts))