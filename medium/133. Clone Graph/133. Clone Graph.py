"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return node

        # new_node = Node()
        # new_node.val = node.val
        # if not node.neighbors:
        #     return new_node
        # # visited = set()
        # nodes_track = {}
        # queue: Deque[Node] = deque([node])
        # nodes_track[node] = new_node
        # while queue:
        #     item = queue.popleft()
        #     neighbors = item.neighbors
        #     for neighbor in neighbors:
        #         if neighbor not in nodes_track:
        #             new_node = Node()
        #             new_node.val = neighbor.val
        #             nodes_track[neighbor] = new_node
        #             queue.append(neighbor)
        #         nodes_track[item].neighbors.append(nodes_track[neighbor])
        # return nodes_track[node]

        visited = {}

        def clone(curr: Node) -> Optional["Node"]:
            if not curr:
                return None

            if curr.val in visited:
                return visited[curr.val]

            copy = Node(curr.val)
            visited[curr.val] = copy

            for neighbor in curr.neighbors:
                copy.neighbors.append(clone(neighbor))

            return copy

        return clone(node)
