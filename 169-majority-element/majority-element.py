class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count = Counter(nums)
        # return count.most_common(1)[0][0]

        # nums.sort()
        # n = len(nums)
        # return nums[n//2]
        
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        for key, value in freq.items():
            if value>len(nums)//2:
                return key
    