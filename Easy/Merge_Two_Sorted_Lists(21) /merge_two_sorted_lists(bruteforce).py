from typing import Optional
from utils import transform_lists_into_linked, iterate_over_linked_list, ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1
        current2 = list2
        counter = 1

        while current1 and current2:
            if counter % 2 == 0:
                nxt = current2.next
                current2.next = current1
                current2 = nxt
                counter +=1
                continue

            nxt = current1.next
            current1.next = current2
            current1 = nxt
            counter +=1
        return list1


solution = Solution()
list1 = [1, 2, 4]
list2 = [1, 3, 5]

transformed = transform_lists_into_linked(list1)
transformed_2 = transform_lists_into_linked(list2)

result = solution.mergeTwoLists(transformed, transformed_2)

iterate_over_linked_list(result)
