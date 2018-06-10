# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return None
        cloned_node = UndirectedGraphNode(node.label)
        cloned, queue = {node:cloned_node}, [node]
        while queue:
            cur = queue.pop()
            for n in cur.neighbors:
                if n not in cloned:
                    cloned_node = UndirectedGraphNode(n.label)
                    cloned[n] = cloned_node
                    queue.append(n)
                cloned[cur].neighbors.append(cloned[n])
                    
        return cloned[node]
            
                
