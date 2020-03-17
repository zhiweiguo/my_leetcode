'''
平衡二叉树
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。
如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    flag = True # 状态标志初始化
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True   

        def cal_deep(root):
            if not root:
                return 0
            left = cal_deep(root.left)
            right = cal_deep(root.right)
            if abs(left - right) > 1:
                self.flag = False
            
            return max(left, right) + 1
        
        cal_deep(root)

        return self.flag