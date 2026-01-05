from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		if head:
			current = head
			prev = None

			while True:
				if current.next is None:
					current.next = prev
					head = current
					return head
				temp_val_2 = current.next
				current.next = prev
				prev = current
				current = temp_val_2





def create_singly_linked_list(some_list: list):
  if not some_list:
    return

  head = ListNode(some_list[0])
  current = head

  for item in some_list[1:]:
    current.next = ListNode(item)
    current = current.next

  return head