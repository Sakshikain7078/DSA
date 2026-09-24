class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            res = sum(int(digit) for digit in str(nums[i]))
            if res == i:
                return i
            
        return -1