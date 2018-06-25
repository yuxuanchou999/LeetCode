class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3: return 0
        dif = A[1] - A[0]
        st, ans = 0, 0
        for i in range(1, len(A)):
            if dif != A[i] - A[i - 1]:
                dif = A[i] - A[i - 1]
                if i - st > 2:
                    ans += (i - st - 2) * (i - st - 1) // 2
                st = i - 1
        
        if len(A) - st > 2:
            ans += (len(A) - st - 2) * (len(A) - st - 1) // 2
        return ans
        
        
