'''
从上到下打印二叉树
    3
   / \
  9  20
    /  \
   15   7

返回：[3,9,20,15,7]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        que = []
        que.append(root)
        while que:
            for i in range(len(que)):
                node = que.pop(0)
                res.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        
        return res
                        
        