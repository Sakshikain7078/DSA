class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        num = []
        for i in nums:
            num.append(i**2)
        return sorted(num)