# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sameTree(self, root1, root2):

        if root1 is None and root2 is None:
            return True
        
        if root1 is not None and root2 is None or root1 is None and root2 is not None:
            return False
        
        queue1 = [root1]
        queue2 = [root2]

        #BFS:
        while (queue1):
            node1 = queue1.pop(0)
            node2 = queue2.pop(0)

            if node1.val != node2.val:
                return False       

            if (node1.left):
                if node2.left:
                    queue1.append(node1.left)
                    queue2.append(node2.left)
                else:
                    return False
            elif (node2.left):
                return False
            
            if (node1.right):
                if node2.right:
                    queue1.append(node1.right)
                    queue2.append(node2.right)
                else:
                    return False
            elif (node2.right):
                return False
            
        return True

    def isSubtree(self, root, subRoot):
        #BFS:

        queue = [root]

        while queue:
            node = queue.pop(0)

            if node.val == subRoot.val and self.sameTree(node, subRoot):
                return True

            if (node.left):
                queue.append(node.left)
            if (node.right):
                queue.append(node.right)

        return False



solution = Solution ()

p = TreeNode(1)
p.left = TreeNode (2)
p.right = TreeNode (3)

q = TreeNode(1)
q.left = TreeNode (2)
q.right = TreeNode (3)
q.right.right = TreeNode (3)

print(solution.isSubtree(p,q))