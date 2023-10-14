class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_letters = [letter for letter in jewels]
        stones_letters = [letter for letter in stones]
        return len([result for result in stones_letters if result in jewel_letters])


solution = Solution()
jewels = "aA"
stones = "aAAbbbb"
print(solution.numJewelsInStones(jewels, stones))