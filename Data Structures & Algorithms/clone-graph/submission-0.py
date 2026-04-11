"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = dict()

        def dfs(node):
            if node and node not in visited:
                clone = Node(node.val)
                visited[node] = clone
                
                for neighbor in node.neighbors:
                    clone.neighbors.append(dfs(neighbor))
                return clone
            return visited.get(node, None)

        return dfs(node)