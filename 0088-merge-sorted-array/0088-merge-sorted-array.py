class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # fill from the end
        pos = m + n - 1
        m -= 1
        n -= 1

        while n >= 0:
        # The goal is to merge all elements from nums2 into nums1.
        # You stop when n < 0 (i.e., all elements from nums2 have been merged)
            if m >= 0 and nums1[m] > nums2[n]:
                nums1[pos] = nums1[m]
                m -= 1
            else:
                nums1[pos] = nums2[n]
                n -= 1
            pos -= 1
