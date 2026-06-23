class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[-1]*len(nums1)
        for i in range(len(nums1)):
            flag=0
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    flag=1
                if flag==1 and nums2[j]>nums1[i]:
                    res[i]=nums2[j]
                    break
        
        return res
                    