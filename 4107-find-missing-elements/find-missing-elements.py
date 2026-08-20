class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res = []
        maxi = max(nums)
        mini = min(nums)
        num = sorted(nums)
        ans = list(range(mini, maxi + 1))
        for x in ans:
            if x not in num:
                res.append(x)
        return res