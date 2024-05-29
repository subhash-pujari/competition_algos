class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([item for item in s.strip().split(" ") if item != ""][::-1])


input = "the sky is blue"

print(Solution().reverseWords(input))
