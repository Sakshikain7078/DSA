class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)

        num = list(set(nums))
        num.sort()
        if len(num)>=3:
            return num[-3]
        else:
            return num[-1]