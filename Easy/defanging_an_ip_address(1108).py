class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")

solution = Solution()
n = "1.1.1.1"
solution.defangIPaddr(n)