class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        half = (len(nums1) + len(nums2))//2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1) - 1

        while True:
            i = (l + r)//2
            j = half - i - 2

            Aleft = nums1[i] if -1 < i < len(nums1) else float('-inf')

            Aright = nums1[i + 1] if -1 < i + 1 < len(nums1) else float('inf')

            Bleft = nums2[j] if -1 < j < len(nums2) else float('-inf')

            Bright = nums2[j + 1] if -1 < j + 1 < len(nums2) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:

                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2
                
                else:
                    return min(Aright, Bright)
            
            if Aleft > Bright:
                r = i - 1

            else:
                l = i + 1
    

