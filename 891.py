class Solution:
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        ans, pow2 = 0, [1]
        for i in range(1, len(A)):
            pow2.append(pow2[-1] * 2 % (10 ** 9 + 7))
            
        for i in range(len(A)):
            ans += A[i] * (pow2[i] - 1) 
            ans -= A[i] * (pow2[len(A) - i - 1] - 1)
            ans %= (10 ** 9 + 7)
        return ans
