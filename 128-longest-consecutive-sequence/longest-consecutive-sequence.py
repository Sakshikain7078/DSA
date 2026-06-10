class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums.sort()
        # if not nums:
        #     return 0
        # res = []
        # for i in range(len(nums)-1):
        #     if nums[i+1] == nums[i]+1:
        #         res.append(nums[i+1])
        # res.append(nums[0])
        # res.sort()
        # return len(res)
        if not nums:
            return 0
        nums.sort()
        longest = 1
        curr = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1]+1:
                curr += 1
            else:
                longest = max(longest,curr)
                curr = 1
        return max(longest,curr)