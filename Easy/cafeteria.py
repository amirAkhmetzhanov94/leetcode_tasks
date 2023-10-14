from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        while sandwiches or count == 3:
            for sandwich in sandwiches:
                for student in students:
                    if student != sandwich:
                        students.append(0)
                    else:
                        students.pop(0)
                        sandwiches.pop(0)
                continue
            count += 1
        return len(students)


students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]
solution = Solution()
print(solution.countStudents(students=students, sandwiches=sandwiches))
