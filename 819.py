class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        para = paragraph.split()
        dic, cnt = collections.defaultdict(int), collections.defaultdict(list)
        for x in para:
            if not x[-1].isalpha():
                dic[x[:-1].lower()] += 1
            else:
                dic[x.lower()] += 1
        
        ans = 0
        for x in dic:
            if x not in banned:
                cnt[dic[x]].append(x)
                ans = max(ans, dic[x])
            
        return cnt[ans][0]
                
        
