class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                if t[i] in dic.values():
                    return False
                else:
                    dic[s[i]] = t[i]
            else:
                if dic[s[i]] == t[i]:
                    continue
                return False
            
        return True
