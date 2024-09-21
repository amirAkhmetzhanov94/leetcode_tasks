class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_pointer = 0
        right_pointer = len(height) - 1
        max_width = 0

        while left_pointer <= right_pointer:
            current_length = len(height[left_pointer:right_pointer])
            if height[left_pointer] > height[right_pointer]:
                width = height[right_pointer] * current_length
                right_pointer -= 1
            else:
                width = height[left_pointer] * current_length
                left_pointer += 1
            if width > max_width:
                max_width = width
        return max_width


solution = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(solution.maxArea(height))