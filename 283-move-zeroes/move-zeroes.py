class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        c = 0
        for num in nums:
            if(num != 0):
                nums[c] = num
                c += 1
        while(c<len(nums)):
            nums[c] = 0
            c += 1