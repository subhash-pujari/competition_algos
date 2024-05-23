"""
Problem: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75
Solved by @Subhash
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        s_10 = [1 if ch in ["a", "e", "i", "o", "u", "y"] else 0 for ch in s ]
        
        # print(s_10)
        # print([s_10[i : i + k] for i in range(len(s_10) - k + 1)])

        max_vowel_count = list()

        for sub_arr in [s_10[i : i + k] for i in range(len(s_10) - k + 1)]:
            
            one_count = list()
            for i, num in enumerate(sub_arr):
                if i == 0:
                    one_count.append(num)
                else:
                    if num == 0:
                        one_count.append(0)
                    else:
                        one_count.append(one_count[i - 1] + 1)
            
            max_vowel_count.append(max(one_count))

        return max(max_vowel_count)

        # return max([sum(s_10[i : i + k]) for i in range(len(s_10) - k - 1)])

print(Solution().maxVowels("abciiidef", 3))
print(Solution().maxVowels("leetcode", 3))
print(Solution().maxVowels("aeiou", 2))

print(Solution().maxVowels("weallloveyou", 7))

