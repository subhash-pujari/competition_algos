from typing import List


class Solution:
    def twoSum(self, nums: List[int]) -> List[int]:
        total_product = 1
        for num in nums:
            total_product *= num

        return [total_product / num if num != 0 else total_product / 1 for num in nums]


print(Solution().twoSum([2, 7, 11, 15]))
