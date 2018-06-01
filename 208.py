class TrieNode(object):
    def __init__(self):
        self.is_string = False
        self.leaves = {}


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for w in word:
            if not w in cur.leaves:
                cur.leaves[w] = TrieNode()
            cur = cur.leaves[w]
        cur.is_string = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.childSearch(word)
        if node:
            return node.is_string
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.childSearch(prefix) is not None
    
    def childSearch(self, word):
        cur = self.root
        for w in word:
            if w in cur.leaves:
                cur = cur.leaves[w]
            else:
                return None
        return cur

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
