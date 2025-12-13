class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        neg = []
        pos = []
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        if not neg:
            return min(pos)
        elif not pos:
            return max(neg)  
        else:
            a = max(neg)
            b = min(pos)
            if abs(a) < abs(b):
                return a
            elif abs(b) < abs(a):
                return b
            else:
                return max(a,b)     