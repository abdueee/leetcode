class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = {}
        res = [-1]*len(nums1)
        
        for i,j in enumerate(nums1):
            nums1_dict[j] = i
        
        for i in range(len(nums2)):
            if nums2[i] not in nums1_dict:
                continue
            
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    ctr = nums1_dict[nums2[i]]
                    res[ctr] = nums2[j]
                    break
        return res