class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        first, second, last, ans = 0, 0, '', 2 ** 31 - 1
        for i in range(len(words)):
            if words[i] == word1:
                if not last: last = word1
                first = i
                if last == word2:   
                    ans = min(ans, first - second)
                    last = word1
                    
            elif words[i] == word2:
                if not last: last = word2
                second = i
                if last == word1:
                    ans = min(ans, second - first)
                    last = word2
        return ans
