# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = []
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        inorder(root)
        new_node = TreeNode(res[0])
        root1 = new_node
        prev = root1
        for i in range(1,len(res)):
            new_Node = TreeNode(res[i])
            prev.right = new_Node
            prev = new_Node

        return root1