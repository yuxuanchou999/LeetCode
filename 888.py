class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        k = sum(A) - sum(B)
        B = set(B)
        for x in A:
            if x - k // 2 in B:
                return [x, x - k // 2]
