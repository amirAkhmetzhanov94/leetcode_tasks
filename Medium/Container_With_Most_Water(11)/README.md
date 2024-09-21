## Problem Statement

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` from `nums` **in-place**. The order of the elements may be changed. Return the number of elements in `nums` which are not equal to `val`.

Consider the number of elements in `nums` which are not equal to `val` to be `k`. To get accepted, you need to do the following:

- Modify the array `nums` such that the first `k` elements contain the elements which are not equal to `val`.
- The remaining elements beyond the first `k` are not important.
- Return `k`.

### Custom Judge:

The judge will test your solution with the following code:

```java
int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // Expected array with no values equal to val and correct length.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}