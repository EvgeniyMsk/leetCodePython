class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        results = [0] * n
        results[0] = 1
        results[1] = 2
        for i in range(2, n, 1):
            results[i] = results[i-1] + results[i-2]
        return results[n - 1]
