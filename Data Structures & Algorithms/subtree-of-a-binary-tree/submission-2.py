# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root,subRoot):
            q=deque([(root,subRoot)])

            while q:
                node1,node2 = q.popleft()
                if not node1 and not node2:
                    continue
                if not node1 or not node2:
                    return False
                if node1.val!=node2.val:
                    return False
                
                q.append((node1.left,node2.left))
                q.append((node1.right,node2.right))
            return True

        queue=deque([root])

        while queue:
            node=queue.popleft()

            if node.val==subRoot.val:
                if sameTree(node,subRoot):
                    return True
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return False
