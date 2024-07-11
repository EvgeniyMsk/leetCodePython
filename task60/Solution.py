class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorials = [1]
        nums = ["1"]
        for i in range(1, n):
            factorials.append(factorials[i - 1] * i)
            nums.append(str(i + 1))
        k = k - 1
        output = []
        for i in range(n - 1, -1, -1):
            idx = k // factorials[i]
            output.append(nums[idx])
            del nums[idx]
            k -= idx * factorials[i]
        return "".join(output)
