class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        num = sorted(set(nums),reverse = True)
        return num[:k]