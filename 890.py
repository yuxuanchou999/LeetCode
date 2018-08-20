class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        for x in words:
        
            dic, j = {}, 0
            for i in range(len(x)):
                if x[i] not in dic:
                    if pattern[i] in dic.values(): break
                    dic[x[i]] = pattern[i]
                elif dic[x[i]] != pattern[i]:
                    break
                j += 1
            if j == len(pattern):
                res.append(x)
        return res
                    
        
                
