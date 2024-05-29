"""
Problem: https://leetcode.com/problems/determine-if-two-strings-are-close/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        arr1 = []
        arr2 = []
        for j in set(word1):
            arr1.append(word1.count(j))
            arr2.append(word2.count(j))
        arr1.sort()
        arr2.sort()
        return arr1 == arr2


word1 = "abc"
word2 = "bca"
print(Solution().closeStrings(word1, word2))

word1 = "a"
word2 = "aa"
print(Solution().closeStrings(word1, word2))

word1 = "cabbba"
word2 = "abbccc"
print(Solution().closeStrings(word1, word2))
