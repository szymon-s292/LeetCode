# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # merge into new binary tree
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root1, root2):
            if not root1 and not root2:
                return None
            if root1 and not root2:
                return root1
            if not root1 and root2:
                return root2

            root1.val += root2.val
            root1.left = dfs(root1.left, root2.left)
            root1.right = dfs(root1.right, root2.right)
            return root1
        return dfs(root1, root2)
  # merge into first binary tree
  def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root1, root2):
            if not root1 and not root2:
                return None
            if root1 and not root2:
                return root1
            if not root1 and root2:
                return root2

            curr = TreeNode(root1.val + root2.val)
            curr.left = dfs(root1.left, root2.left)
            curr.right = dfs(root1.right, root2.right)
            return curr
        return dfs(root1, root2)
