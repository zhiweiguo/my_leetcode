'''
二叉搜索树的第K大节点

二叉搜索树特点说明：
1.若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
2.若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值；
3.任意节点的左、右子树也分别为二叉查找树；
4.没有键值相等的节点。

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        '''
        递归方法实现
        '''
        self.res = None
        self.count = k
        
        def kth(node):
            if not node:
                return
            kth(node.right)
            self.count -= 1
            if self.count == 0:
                self.res = node.val
                return 
            kth(node.left)
        
        kth(root)

        return self.res

    def kthLargest_2(self, root, k):
        '''
        迭代方法实现：
        '''
        # 待补充

        return 
