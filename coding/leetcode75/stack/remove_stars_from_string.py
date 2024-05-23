
"""
Problem: https://leetcode.com/problems/removing-stars-from-a-string/description/?envType=study-plan-v2&envId=leetcode-75
"""

class Solution_Subhash:
    def removeStars(self, s: str) -> str:
        stack = list()
        # input_str = "leet**cod*e"
        
        for ch in s:

            if ch == "*":
                if len(stack):
                    stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)


"""
Solution: https://leetcode.com/problems/removing-stars-from-a-string/solutions/4145219/python3-c-solution/?envType=study-plan-v2&envId=leetcode-75
"""
class Solution1:
    def removeStars(self, s: str) -> str:
        res = ""
        to_remove = 0
        # Represents number of symbols we will skip
        # when meet
        for symb in s[::-1]:
            if symb == "*":
                to_remove += 1
                # Skip one more symbol when meet
            else:
                if not to_remove:
                # if to_remove == 0
                    res += symb
                else:
                    to_remove -= 1
                    # Skipping a symbol
        return res[::-1]
        # The recieved string is also reversed, so
        # reverse it to get the answer