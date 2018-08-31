class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        ans, cnt, k = 0, 0, None
        while N:
            if N % 2 == 1:
                if k != None and ans < cnt - k:
                    ans = cnt - k
                k = cnt
            cnt += 1
            N //= 2
        return ans
                
