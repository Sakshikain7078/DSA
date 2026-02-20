class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     if nums[i-1]<nums[i]>nums[i+1]:
        #         return i
        # if len(nums)
        return nums.index(max(nums))