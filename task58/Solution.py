class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        position = len(s) - 1
        while position >= 0 and s[position] == " ":
            position -= 1
        length = 0
        while position >= 0 and s[position] != " ":
            position -= 1
            length += 1
        return length
