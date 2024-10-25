# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        values_list = []
        current = head
        while current.next:
            values_list.append(current.val)
            current = current.next
        values_list.append(current.val)
        return values_list[::-1]



solution = Solution()
head = [1, 2, 3, 4, 5]


def transform_list(list_of_values: list):
    if not list_of_values:
        return

    head = ListNode(val=list_of_values[0])
    current = head

    for value in list_of_values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


linked_list = transform_list(head)
print(solution.reverseList(linked_list))