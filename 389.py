class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {x:s.count(x) for x in set(s)}
            
        for x in t:
            if x not in dic:
                return x
            else:
                if dic[x] != t.count(x):
                    return x
            
        
        
