class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # med = median(sorted(nums1+nums2))
        # return med


        num = sorted(nums1+nums2)
        
        if len(num) % 2 == 1:
            return float(num[len(num)//2])
        else:
            return (num[len(num)//2-1] + num[len(num)//2])/2.0