class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1]*n
        for i in range(n):
            idx = nums[i]
            if idx!=0:
                res[i] = nums[(i+idx)%n]
            else:
                res[i]=nums[i]
        return res