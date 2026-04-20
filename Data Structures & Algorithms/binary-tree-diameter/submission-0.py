# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia = 0

        def Height(node):
            if node is None:
                return 0
            light_Height= Height(node.left)
            right_Height = Height(node.right)

            self.dia = max(self.dia,light_Height + right_Height)

            return 1 + max(light_Height, right_Height)
        
        Height(root)
        return self.dia