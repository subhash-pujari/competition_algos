"""
https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75
@author: Subhash
"""

class Solution:
    
    def isSubsequence(self, s: str, t: str) -> bool:
        
        ch_index = dict([(ch, i) for i, ch in enumerate(t)])

        ch_index_substr = list()

        for ch in s:
            if ch not in ch_index:
                return False
            else:
                ch_index_substr.append(ch_index[ch])

        for i in range(len(ch_index_substr)):

            if i == len(ch_index_substr) - 1:
                return True
            
            if ch_index_substr[i + 1] < ch_index_substr[i]:
                return False

s = "abc"
t = "ahbgdc"

print(Solution().isSubsequence(s, t))