class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        c = collections.Counter(words)
        candidates = list(set(words))
        candidates.sort(key=lambda x: (-c[x], x))
        return candidates[:k]
            
                
            
