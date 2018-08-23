class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if B in A: return 1
        if len(A) >= len(B):
            return 2 if B in A + A else -1
        else:
            n = len(B) // len(A)
            if B in n * A: return n
            elif B in (n + 1) * A: return n + 1
            elif B in (n + 2) * A: return n + 2
            return -1
