"""
Problem: https://leetcode.com/problems/increasing-triplet-subsequence/submissions/1264774403/?envType=study-plan-v2&envId=leetcode-75
Solution from Subhash, still issue in runtime.
"""

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            imp_nums = list()

            for j in range(i, len(nums)):
                # if i not in indexes:
                for imp_num in imp_nums:
                    if imp_num < nums[j]:
                        return True

                if nums[i] < nums[j]:
                    imp_nums.append(nums[j])

        return False


print(Solution().increasingTriplet([1, 2, 3, 4, 5]))
print(Solution().increasingTriplet([5, 4, 3, 2, 1]))
print(Solution().increasingTriplet([2, 1, 5, 0, 4, 6]))
