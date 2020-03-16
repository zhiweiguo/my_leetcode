'''
二叉树的最近公共祖先
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = None
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def recurse_node(cur_node):
            if not cur_node:
                return False
            
            left = recurse_node(cur_node.left)
            right = recurse_node(cur_node.right)
            mid = (cur_node == p or cur_node == q)
            if left+right+mid >= 2:
                self.ans = cur_node 
            return left or right or mid

        recurse_node(root)
        return self.ans

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        递归法：
        '''
        if (not root) or (root == p) or (root == q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        
        return root