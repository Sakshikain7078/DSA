class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        res =  []
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                res.append(nums[i])
        l = n*(n+1)//2
        m = sum(set(nums))
        miss = l - m
        res.append(miss)
        return res