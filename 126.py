class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList: return []
        dic, level, parents = set(wordList), set([beginWord]), collections.defaultdict(set)
        while level and endWord not in parents:
            next_level = collections.defaultdict(set)
            for w in level:
                for x in 'abcdefghijklmnopqrstuvwxyz':
                    for i in range(len(beginWord)):
                        cand = w[:i] + x + w[i + 1:]
                        if cand not in parents and cand in dic:
                            next_level[cand].add(w)
            level = next_level
            parents.update(level)
        res = [[endWord]]
        while res and res[0][0] != beginWord:
            res = [[p] + r for r in res for p in parents[r[0]]]
        return res
        
