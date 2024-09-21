## Problem Statement

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates **in-place** such that each unique element appears only once. The relative order of the elements should be kept the same. Return the number of unique elements in `nums`.

To meet the requirements, you need to:
- Modify the array `nums` such that the first `k` elements of `nums` contain the unique elements in the original order.
- The remaining elements of `nums` beyond the first `k` are irrelevant.
- Return the value of `k`, which represents the number of unique elements.

### Example 1

**Input:** `nums = [1,1,2]`

**Output:** `2`

**Explanation:** 
- After removing duplicates, `nums` becomes `[1,2,_]` where `k = 2`. The underscores represent elements beyond the returned `k`.

### Example 2

**Input:** `nums = [0,0,1,1,1,2,2,3,3,4]`

**Output:** `5`

**Explanation:** 
- After removing duplicates, `nums` becomes `[0,1,2,3,4,_,_,_,_,_]` where `k = 5`.

### Constraints

- `1 <= nums.length <= 30,000`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in non-decreasing order.
