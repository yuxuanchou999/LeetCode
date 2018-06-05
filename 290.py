class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dic = {}
        if ' ' in str:
            str = str.split(' ')
        else:
            if len(pattern) == 1:
                return True
            return False
        if len(str) != len(pattern): return False  
        for i in range(len(pattern)):
            if pattern[i] not in dic:
                if str[i] in dic.values():
                    return False
                dic[pattern[i]] = str[i]
            else:
                if dic[pattern[i]] != str[i]:
                    return False
        return True
                
        
            
