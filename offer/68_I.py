'''
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        利用二叉搜索树的特点进行查找
        '''
        if p.val > q.val:
            p, q = q, p

        def sub(root):
            if not root:
                return None
            if p.val <= root.val and q.val >= root.val:
                return root
            res = sub(root.left)
            res = res or sub(root.right)
            return res
        
        return sub(root)


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    res1 = node1 or node2
    res2 = None or node2
    res3 = node1 or None
    print(res1, res2, res3)
    res4 = (res1 == node1)
    res5 = (res2 == node2)
    print(res4, res5)