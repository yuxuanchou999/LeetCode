class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.cap = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def insert(self, node):
        tmp = self.tail.prev
        tmp.next = node
        self.tail.prev = node
        node.prev = tmp
        node.next = self.tail
        self.cache[node.key] = node
    
    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev, node.next = None, None
        self.cache.pop(node.key)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        val = self.cache[key].val
        self.delete(self.cache[key])
        self.insert(Node(key, val))
        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.delete(self.cache[key])
        elif len(self.cache) == self.cap:
            self.delete(self.head.next)
        node = Node(key, value)
        self.insert(node)


