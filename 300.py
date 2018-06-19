class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def insert(n):
            left, right = 0, len(LIS) - 1
            while left <= right:          #find the first LIS[left] >= n
                mid = (left + right) // 2
                if LIS[mid] >= n:
                    right = mid - 1
                else:
                    left = mid + 1
            if left == len(LIS): LIS.append(n)
            else: LIS[left] = n
                
        LIS = []
        for n in nums:
            insert(n)
        return len(LIS)
