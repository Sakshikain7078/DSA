class Solution:
    def getMinDistance(self, nums, target, start):
        res = len(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                res = min(res,abs(i-start))
        return res