class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ans = 0
        words.sort(key = lambda x : len(x), reverse = True)
        dic = {x:set(x) for x in words}
        for i in range(len(words)):
            if len(words[i]) ** 2 <= ans: break
            for j in range(i + 1, len(words)):
                if not (dic[words[i]] & dic[words[j]]):
                    ans = max(ans, len(words[i]) * len(words[j]))
                    break
                    
        return ans
