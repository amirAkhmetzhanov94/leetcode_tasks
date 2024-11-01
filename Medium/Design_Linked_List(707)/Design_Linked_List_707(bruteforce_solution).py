class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList(object):

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        current = self.head
        length_count = 0
        while current:
            if length_count == index:
                return current.val
            previous_current = current
            current = current.next
            length_count += 1
        if length_count == index:
            return previous_current.val
        return -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        old_head = self.head
        self.head = ListNode(val=val, next=old_head)

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        current = self.head
        while current.next:
            current = current.next
        current.next = ListNode(val=val)
        self.tail = current.next

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None

        void addAtIndex(int index, int val) Add a node of value val before the index'th node in the linked list.
        If index equals the length of the linked list, the node will be appended to the end of the linked list.
        If index is greater than the length, the node will not be inserted.

        """
        current = self.head
        length_counter = 0
        while current.next:
            if index == (length_counter + 1):
                old_current_next = current.next
                current.next = ListNode(val, next=old_current_next)
                return current
            current = current.next
            length_counter += 1
        if index == length_counter:
            current.next = ListNode(val)
            return current
        return

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        current = self.head
        length_count = 0
        while current:
            if index == length_count:
                self.head = current.next
                return
            current = current.next
            length_count += 1
        return


list_of_operations = ["MyLinkedList", "addAtHead", "addAtHead", "addAtHead", "addAtIndex", "deleteAtIndex", "addAtHead",
                      "addAtTail", "get", "addAtHead", "addAtIndex", "addAtHead"]
list_of_numbers = [[], [7], [2], [1], [3, 0], [2], [6], [4], [4], [4], [5, 0], [6]]

for operation, args in zip(list_of_operations, list_of_numbers):
    if operation == 'MyLinkedList':
        linked_list = MyLinkedList()
        continue
    result = getattr(linked_list, operation)(*args)
    print(result)
