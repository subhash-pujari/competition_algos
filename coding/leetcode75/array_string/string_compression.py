"""
Problem with the question in leetcode.
Problem: https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75
"""

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        curr_ch = None
        curr_ch_count = 0
        s = ""

        for ch in chars:
            if curr_ch is None:
                # s = ch
                curr_ch = ch
                curr_ch_count = 1
            else:
                if ch == curr_ch:
                    curr_ch_count += 1
                else:
                    if curr_ch_count == 1:
                        s += curr_ch
                        curr_ch_count = 1
                        curr_ch = ch
                    else:
                        s += curr_ch + str(curr_ch_count)
                        curr_ch_count = 1
                        curr_ch = ch

        if curr_ch_count == 1:
            s += curr_ch
            curr_ch_count = 1
            curr_ch = ch
        else:
            s += curr_ch + str(curr_ch_count)
            curr_ch_count = 1
            curr_ch = ch

        return [item for item in s]


print(Solution().compress(["a", "a", "b", "b", "c", "c", "c"]))
print(Solution().compress(["a"]))
print(
    Solution().compress(
        ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    )
)
