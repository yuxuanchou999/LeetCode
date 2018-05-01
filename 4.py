class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # nums = nums1 + nums2
        # nums.sort()
        # l = len(nums)
        # if l%2:
        #     m = nums[l//2]
        # else:
        #     m = 0.5*(nums[l//2] + nums[l//2-1])
        # return float(m)
        l1, l2 = len(nums1), len(nums2)
        if (l1 + l2)%2 == 1:
            return self.getKth(nums1, nums2, (l1 + l2)//2)/1.0
        else:
            return (self.getKth(nums1, nums2, (l1 + l2)//2) + self.getKth(nums1, nums2, (l1 + l2)//2 - 1))/2.0
    
    def getKth(self, A, B, k):
        if len(A) > len(B):
            A, B = B, A
        if not A:
            return B[k]
        if k == len(A) + len(B) - 1:
            return max(A[-1], B[-1])
        i = min(len(A) - 1, k//2)
        j = min(len(B) - 1, k - i)
        if A[i] > B[j]:
            return self.getKth(A[:i], B[j:], i)
        else:
            return self.getKth(A[i:], B[:j], j)
