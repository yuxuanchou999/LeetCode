class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = {}
        l, a = len(s), []
        for i in range(l):
            if i + 9 < l:
                if s[i:i + 10] in dic:
                    if dic[s[i:i + 10]] == 1:
                        a.append(s[i:i + 10])
                    dic[s[i:i + 10]] += 1
                else:
                    dic[s[i:i + 10]] = 1
            else:
                break
        return a
