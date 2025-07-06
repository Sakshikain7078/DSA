class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        l = -1
        for i in count:
            if count[i] == i:
                l = max(l, i)
        return l
