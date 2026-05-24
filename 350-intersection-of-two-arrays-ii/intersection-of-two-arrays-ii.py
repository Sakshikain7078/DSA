class Solution:
    def intersect(self, nums1, nums2):
        res = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                res.append(nums1[i])
                nums2.remove(nums1[i])
        return list((res))
