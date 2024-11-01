# Problem Statement

Design a singly linked list with the following operations:

- `get(index)`: Get the value of the `index`-th node in the linked list. If the index is invalid, return `-1`.
- `addAtHead(val)`: Add a node of value `val` before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
- `addAtTail(val)`: Append a node of value `val` to the last element of the linked list.
- `addAtIndex(index, val)`: Add a node of value `val` before the `index`-th node in the linked list. If `index` equals the length of the linked list, the node will be appended to the end. If `index` is greater than the length, the node will not be inserted.
- `deleteAtIndex(index)`: Delete the `index`-th node in the linked list, if the index is valid.

## Example

**Input:**  
```
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]  
[[], [1], [3], [1, 2], [1], [1], [1]]
```

**Output:**  
```
[null, null, null, null, 2, null, 3]
```

**Explanation:**  
```
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);         // Linked list becomes 1
myLinkedList.addAtTail(3);         // Linked list becomes 1->3
myLinkedList.addAtIndex(1, 2);     // Linked list becomes 1->2->3
myLinkedList.get(1);               // Returns 2
myLinkedList.deleteAtIndex(1);     // Now the linked list is 1->3
myLinkedList.get(1);               // Returns 3
```

## Constraints

- `0 <= index, val <= 1000`
- Methods `get`, `addAtHead`, `addAtTail`, `addAtIndex`, and `deleteAtIndex` can be called up to `2000` times.