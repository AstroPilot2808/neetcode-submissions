"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def clone(node):
            if node in oldToNew:
                return oldToNew[node]
            new = Node(node.val)
            oldToNew[node] = new
            for neighbor in node.neighbors:
                new.neighbors.append(clone(neighbor))
            return new
        
        return clone(node) if node else None


