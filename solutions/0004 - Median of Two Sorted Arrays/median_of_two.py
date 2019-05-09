class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        li = sorted(nums1 + nums2)
        length = len(li)
        return float(li[(length - 1) // 2]) if length % 2 == 1 else (li[(length//2) - 1] + li[length//2]) / 2
