class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i

            if nums[i] > target:
                return i
        if target not in nums:
                return len(nums)