class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        full_list = nums1 + nums2
        full_list.sort()
        median_list = len(full_list)/2
        if len(full_list) % 2 == 1:
            median = full_list[int(median_list)]
        else:
            med1 = int(median_list + 0.5)
            med2 = int(median_list - 0.5)
            median = (full_list[med1] + full_list[med2])/2
            
        return median
        
