class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res, first, i = '', (len(S) - S.count('-')) % K, 0
        if not first: first = K
        while i < len(S) and len(res) < first:
            if S[i] != '-':
                res += S[i].upper()
            i += 1
        res += '-'
        cnt = 0
        for j in range(i, len(S)):
            if cnt == K:
                res += '-'
                cnt = 0
            if S[j] != '-':
                res += S[j].upper()
                cnt += 1
        
        return res if res[-1] != '-' else res[:-1]
                
        
