
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# class Solution:
#     def cloneGraph(self, node):
#         if not node:
#             return None
        
#         queue = [node]
#         visitedNodes = set()

#         NewNode = Node(node.val)
#         newQueue = [NewNode]

#         while (queue):
#             n = queue.pop(0)
#             visitedNodes.add(n.val)

#             newNode = newQueue.pop(0)


#             for neighbor in n.neighbors:

#                 newNode.neighbors.append(Node(neighbor.val))



#                 if neighbor.val not in visitedNodes:
#                     queue.append(neighbor)
#                     newQueue.append(newNode)

#         return NewNode

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        
        visited = {}

        def dfs (original_node):
            if original_node in visited:
                return visited[original_node]

            cloned_node = Node(original_node.val)
            visited[original_node] = cloned_node

            for neighbor in original_node.neighbors:
                cloned_neighbor = dfs(neighbor)
                cloned_node.neighbors.append(cloned_neighbor)
   
            return cloned_node
        
        return dfs (node)





solution = Solution()

root = Node(1)

node2 = Node(2)
node5 = Node(5)

root.neighbors.append(node2)
root.neighbors.append(node5)


newRoot = solution.cloneGraph(root)

queue = [newRoot]
visitedNodes = set()

while queue:
    n = queue.pop(0)
    visitedNodes.add(n.val)
    for neighbor in n.neighbors:
        if neighbor.val not in visitedNodes:
            queue.append(neighbor)


# 1 - 2 - 3
# |   |   |
# 5   6 - 7
# 
# 
# 
# 
# 
# 
# 
