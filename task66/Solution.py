from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        dec = 0
        if (digits[len(digits) - 1] + 1) >= 10:
            dec = 1
        for i in range(len(digits)-1, -1, -1):
            result.append((digits[i] + dec * (len(digits) != i + 1) + 1 * (len(digits) == i + 1)) % 10)
            if digits[i] + dec >= 10:
                dec = 1
            else:
                dec = 0
        if (dec == 1):
            result.append(1)
        result.reverse()
        return result
