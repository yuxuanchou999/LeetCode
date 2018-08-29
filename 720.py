class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        dic, l = collections.defaultdict(list), max(len(x) for x in words)
        for x in sorted(words):
            dic[len(x)].append(x)
        
        pre = dic[1]
        for i in range(2, l + 1):
            res = []
            for x in dic[i]:
                if x[:i - 1] in pre:
                    res.append(x)
            if res: pre = res
            else: break
                
        return pre[0]
            
            
        
        
