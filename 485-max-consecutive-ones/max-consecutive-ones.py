class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        res = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
                if count > res:
                    res = count
            else:
                count = 0
        return res