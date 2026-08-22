class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        num = sorted(nums)
        i = num[-2]
        j = num[-1]
        res = (i-1)*(j-1)
        return res