class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        distance, cur, visited, lookup = 0, [beginWord], set([beginWord]), set(wordList)
        
        while cur:
            next_queue = []
            for word in cur:
                if word == endWord:
                    return distance + 1
                for i in range(len(word)):
                    for j in 'qwertyuioplkjhgfdsamnbvcxz':
                        candidate = word[:i] + j + word[i + 1:]
                        if candidate not in visited and candidate in lookup:
                            visited.add(candidate)
                            next_queue.append(candidate)
            
            distance += 1
            cur = next_queue
        
        return 0
