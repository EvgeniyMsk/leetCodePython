import re


class Solution(object):
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n - 1):
            s = re.sub(r"(.)\1*", lambda m: str(len(m.group(0))) + m.group(1), s)
        return s