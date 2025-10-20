class Solution(object):
    def merge(self, nums1, n, nums2, m):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        pos = m + n - 1
        for pos in range(pos, -1, -1):
            if n == 0:
                nums1[pos] = nums2[m - 1]
                m -= 1
            elif m == 0:
                nums1[pos] = nums1[n - 1]
                n -= 1
            else:
                if nums1[n - 1] > nums2[m - 1]:
                    nums1[pos] = nums1[n - 1]
                    n -= 1
                else:
                    nums1[pos] = nums2[m - 1]
                    m -= 1
        return


        