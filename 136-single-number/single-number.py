class Solution(object):
    def singleNumber(self, nums):
        Num = 0
        for i in nums:
            Num ^= i
        return Num