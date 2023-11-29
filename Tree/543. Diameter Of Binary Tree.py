# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [0]

        def dfs(root):
            if not root: ## if not children, the height = -1
                return -1
            
            left = dfs(root.left) ## recursive call on the left child, get height
            right = dfs(root.right) ## recursive call on the right child, get height

            ## diameter = 2 + left height + right height
            result[0] = max(result[0], 2 + left + right) 

            return 1 + max(left, right) ## return height 

        dfs(root)
        return result[0]