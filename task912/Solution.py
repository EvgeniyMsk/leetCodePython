from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        counting = [0] * (2 * 50_000 + 1)
        for num in nums:
            counting[num + 50_000] += 1
        writeInd = 0
        for i in range(0, len(counting), 1):
            freq = counting[i]
            while freq != 0:
                nums[writeInd] = i - 50_000
                writeInd += 1
                freq -= 1
        return nums
