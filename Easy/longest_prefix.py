from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0
        result = ""
        while count < len(min(strs)):
            words = {word[count] for word in strs}
            if len(words) == 1:
                result += "".join(words)
                count +=1
            else:
                return result
        return result


strs = ["flower", "flow", "flight"]
strs2 = ["aa", "aa"]
strs4 = ["dog", "racecar", "car"]
strs3 = ["", ""]
strs5 = ["a"]
strs6 = ["ab", "a"]
strs7 = ["flower","flower","flower","flower"]
strs8 = ["aaa","aa","aaa"]
strs9 = ["aac","a","ccc"]
solution = Solution()
print(solution.longestCommonPrefix(strs))
