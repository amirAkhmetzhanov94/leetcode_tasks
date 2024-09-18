class Solution:
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums + nums

solution = Solution()
nums = [1,2,1]
print(solution.getConcatenation(nums))
