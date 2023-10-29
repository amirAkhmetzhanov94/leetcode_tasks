class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        numbers_dict = {}
        result_list = []

        for index, size in enumerate(groupSizes):
            numbers_dict.setdefault(size, []).append(index)

            if len(numbers_dict[size]) == size:
                result_list.append(numbers_dict[size])
                numbers_dict[size] = []

        return result_list


solution = Solution()
print(solution.groupThePeople(groupSizes=[3, 3, 3, 3, 3, 1, 3]))
print(solution.groupThePeople(groupSizes=[2, 1, 3, 3, 3, 2]))
print(solution.groupThePeople(groupSizes=[2, 2, 1, 1, 1, 1, 1, 1]))
print(solution.groupThePeople(
    groupSizes=[16, 11, 15, 11, 6, 9, 11, 10, 17, 22, 16, 22, 17, 10, 12, 11, 11, 11, 6, 17, 8, 10, 10, 10, 11, 8, 10,
                22, 13, 13, 9, 11, 8, 10, 13, 9, 11, 11, 22, 11, 11, 10, 11, 10, 16, 6, 8, 10, 11, 17, 16, 11, 11, 12,
                13, 10, 11, 11, 11, 11, 22, 11, 16, 10, 17, 22, 12, 17, 10, 11, 11, 22, 16, 8, 10, 10, 10, 10, 10, 11,
                12, 9, 10, 11, 16, 15, 22, 10, 10, 17, 15, 13, 11, 11, 9, 9, 10, 10, 11, 10, 15, 8, 15, 11, 11, 8, 10,
                11, 15, 10, 10, 12, 11, 11, 9, 10, 22, 11, 15, 11, 22, 8, 11, 9, 17, 16, 10, 10, 11, 12, 22, 11, 11, 11,
                22, 10, 11, 15, 10, 6, 11, 13, 13, 17, 8, 13, 10, 9, 11, 8, 12, 9, 11, 8, 9, 11, 11, 22, 22, 22, 10, 13,
                8, 11, 11, 6, 11, 16, 11, 10, 22, 16, 10, 17, 11, 11, 10, 10, 16, 12, 10, 16, 15, 15, 13, 11, 12, 22,
                22, 11, 11, 16, 13, 11, 11, 11, 10, 11, 10, 9, 11, 13, 11, 9, 17, 17, 6, 10, 9, 13, 11, 10, 9, 11, 12,
                10, 22, 10, 12, 8, 11, 11, 11, 15, 17, 22, 22, 10, 8, 8, 11, 10, 10, 8, 11, 15, 15, 15, 11, 11, 22, 11,
                17, 11, 9, 17, 16, 16, 9, 10, 10, 11, 17, 11, 17, 12, 11, 9, 11, 15, 16, 11]))
