## Problem Statement

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` **in-place**. The order of the elements may be changed. Return the number of elements in `nums` that are not equal to `val`.

To meet the requirements, you need to:
- Modify the array `nums` such that the first `k` elements of `nums` contain the elements that are not equal to `val`.
- The remaining elements of `nums` beyond the first `k` are irrelevant.
- Return the value of `k`, which represents the number of elements not equal to `val`.

### Example 1

**Input:** `nums = [3,2,2,3]`, `val = 3`

**Output:** `2`

**Explanation:** 
- After removing all occurrences of `3`, `nums` becomes `[2,2,_,_]` where `k = 2`. The underscores represent elements beyond the returned `k`.

### Example 2

**Input:** `nums = [0,1,2,2,3,0,4,2]`, `val = 2`

**Output:** `5`

**Explanation:** 
- After removing all occurrences of `2`, `nums` becomes `[0,1,3,0,4,_,_,_]` where `k = 5`. The order of the first `k` elements can be different, but they must not include `val`.

### Constraints

- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`
