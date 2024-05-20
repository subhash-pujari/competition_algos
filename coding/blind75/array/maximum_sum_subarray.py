import numpy as np

class Solution_Kandane:
    def maxSubArray(self, nums):
        cur_max, max_till_now = 0, -float('inf')
        for c in nums:
            cur_max = max(c, cur_max + c)
            max_till_now = max(max_till_now, cur_max)
        return max_till_now
    
print(Solution_Kandane().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(Solution_Kandane().maxSubArray([5,4,-1,7,8]))
