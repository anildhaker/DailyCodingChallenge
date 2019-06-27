class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_lst = []
        for i in nums1:
            for j in nums2 :
                if i < j:
                    merged_lst.append(i)
                else:
                    merged_lst.append(j)
                    
        l = len(merged_lst)           
        if len(merged_lst)%2 != 0:
            return merged_lst[int((l+1)/2)]
        else:
            return 0.5*(merged_lst[int(l-1//2)] + merged_lst[int((l)//2)])
            

