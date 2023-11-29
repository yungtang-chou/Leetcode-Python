## Solution 1: DFS
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
## Solution 2: BFS
from collections import deque

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        ### initiate counter and queue
        levels = 0
        queue = deque([root])

        while queue:
            for i in range(len(queue)):
                num = queue.popleft() ## find the leftmost value
                if num.left: ## if there are childen for this node, append the nodes 
                    queue.append(num.left)
                if num.right: ## if there are childen for this node, append the nodes 
                    queue.append(num.right)

            levels += 1 ## done looping through a new level
        
        return levels