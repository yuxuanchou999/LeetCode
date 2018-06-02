class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words or len(s) < len(words) * len(words[0]): return [] 
        l, l1, l2 = len(words[0]) * len(words), len(words[0]) , len(words)
        res, lookup = [], collections.defaultdict(int)
        for i in words:
            lookup[i] += 1
            
        for i in range(len(s) - l + 1):
            cur, j = collections.defaultdict(int), 0
            while j < l2:
                word = s[i + j * l1:i + j * l1 + l1]
                if word not in lookup:
                    break
                cur[word] += 1
                if cur[word] > lookup[word]:
                    break
                j += 1
            if j == l2:
                res.append(i)

        return res
                
            
        
