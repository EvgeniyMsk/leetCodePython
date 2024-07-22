from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        if n == 1:
            return
        # Если массив отсортирован, то просто меняем местами
        # два последних значения
        if all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)):
            nums[n - 1], nums[n - 2] = nums[n - 2], nums[n - 1]
            return

        index = n - 1
        found = False
        for i in range(n - 2, -1, -1):
            index -= 1
            if nums[i] < nums[i + 1]:
                found = True
                break
        if index == 0 and not found:
            for i in range(0, n // 2, 1):
                nums[i], nums[n - i - 1] = nums[n - i - 1], nums[i]
            return
        index2 = -1
        for i in range(n - 1, index, -1):
            if nums[i] > nums[index]:
                index2 = i
                break
        nums[index], nums[index2] = nums[index2], nums[index]
        nums[index + 2: index2].sort()


sol = Solution()

nums = [1, 2, 3]


# print(len(nums) // 2)
print(nums)
sol.nextPermutation(nums)
print(nums)
sol.nextPermutation(nums)
print(nums)
sol.nextPermutation(nums)
print(nums)
sol.nextPermutation(nums)
print(nums)
sol.nextPermutation(nums)
print(nums)
sol.nextPermutation(nums)
print(nums)
