from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        map = {}
        for i in range(len(heights)):
            map[heights[i]] = names[i]
        heights.sort(reverse=True)
        for i in range(len(names)):
            names[i] = map[heights[i]]
        return names
