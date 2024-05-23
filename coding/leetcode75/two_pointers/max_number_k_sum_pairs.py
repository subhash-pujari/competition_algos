from typing import List

class Solution_onepass_wout_sort:
    def maxOperations(self, nums: List[int], k: int) -> int:
        from collections import defaultdict

        # int gives 0 when not found
        complements = defaultdict(int)
        ops = 0
        for n in nums:
            if complements[n] > 0:
                ops += 1
                complements[n] -= 1
            elif n < k:
                complement = k - n
                complements[complement] += 1
        return ops


class Solution_two_pointer_wth_sort:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0 
        right = len(nums) - 1
        operation = 0 

        while left < right:
            if ((nums[left] + nums[right]) == k):
                operation += 1
                left +=1 
                right -=1
            elif((nums[left] + nums[right]) < k):
                left += 1
            else:
                right -= 1
        return operation


print(Solution_onepass_wout_sort().maxOperations([1,2,3,4], 5))
print(Solution_onepass_wout_sort().maxOperations([3,1,3,4,3], 6))


print(Solution_two_pointer_wth_sort().maxOperations([1,2,3,4], 5))
print(Solution_two_pointer_wth_sort().maxOperations([3,1,3,4,3], 6))

