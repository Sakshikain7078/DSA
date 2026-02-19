class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i  
        if target not in nums:
            if target<nums[0]:
                return 0
            if target>nums[len(nums)-1]:
                return len(nums)
            else:
                for n in range(len(nums)):
                    if nums[n]>target:
                        return n