from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pos = 0
        for i in range(len(nums)):
            if target > nums[i] and pos <= len(nums) - 1:
                pos += 1
        return pos
