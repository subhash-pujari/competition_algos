"""
Problem: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=study-plan-v2&envId=leetcode-75
Solution:
"""

from typing import List


def longestSubarray(nums: List[int]) -> int:
    left, right = 0, 0
    k = 1
    for right in range(len(nums)):
        if nums[right] == 0:
            k -= 1
        if k < 0:
            if nums[left] == 0:
                k += 1
            left += 1
    return right - left


print(longestSubarray([1, 1, 0, 1]))
print(longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))
