class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        return -1


solution = Solution()
haystack = "aaaaaa"
needle = "bba"
print(solution.strStr(haystack, needle))