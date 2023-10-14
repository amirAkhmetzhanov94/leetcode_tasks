# Definition for singly-linked list.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = []
        if list1 is not None:
            while list1.next is not None:
                new_list.append(list1.val)
                list1 = list1.next
            new_list.append(list1.val)
        if list2 is not None:
            while list2.next is not None:
                new_list.append(list2.val)
                list2 = list2.next
            new_list.append(list2.val)
        if not new_list:
            return ListNode(val="", next=None)
        new_list.sort()
        new_list_node = ListNode(new_list[0])
        head = new_list_node
        for i in new_list[1:]:
            temp = ListNode(i)
            new_list_node.next = temp
            new_list_node = temp
        return head




listnode1 = ListNode(1, ListNode(2, ListNode(4)))
listnode2 = ListNode(1, ListNode(3, ListNode(4)))
solution = Solution()
solution.mergeTwoLists(listnode1, listnode2)