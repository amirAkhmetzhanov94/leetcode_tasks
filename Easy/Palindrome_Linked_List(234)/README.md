## Problem Statement

Given the `head` of a singly linked list, determine whether the list is a **palindrome**.

A linked list is a palindrome if it reads the same forward and backward.

Return `true` if it is a palindrome, otherwise return `false`.

To meet the requirements, you should aim to:
- Use **O(n)** time.
- Use **O(1)** extra space (i.e., do it in-place if possible).

---

### Example 1

**Input:** `head = [1,2,2,1]`

**Output:** `true`

**Explanation:**  
- Reading from left to right: `1 → 2 → 2 → 1`  
- Reading from right to left: `1 → 2 → 2 → 1`  
- They match, so the list is a palindrome.

---

### Example 2

**Input:** `head = [1,2]`

**Output:** `false`

**Explanation:**  
- Forward: `1 → 2`  
- Backward: `2 → 1`  
- They do not match, so it is not a palindrome.

---

### Constraints

- The number of nodes in the list is in the range `[1, 100,000]`
- `0 <= Node.val <= 9`
