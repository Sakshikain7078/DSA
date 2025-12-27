class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stk = []
        for i in range(len(nums1)):
            res = -1
            for j in range(len(nums2)):
                if nums2[j] == nums1[i]:
                    for k in range(j+1,len(nums2)):

                        if nums2[k] > nums1[i]:
                            res = nums2[k]
                            break
                    break
            stk.append(res)
        return stk