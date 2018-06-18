class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for x in nums1:
            i = nums2.index(x) + 1
            while i < len(nums2):
                if nums2[i] > x:
                    res.append(nums2[i])
                    break
                i += 1
            if i == len(nums2): res.append(-1)
        return res
