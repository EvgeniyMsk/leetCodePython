from typing import List, Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        print(sorted(nums, key=lambda x: (x)))
        return sorted(nums, key=lambda x: (x, x))
