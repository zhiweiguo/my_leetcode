'''
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        '''
        递归法
        '''
        def sub(left, right):
            # 判断两节点是否均为None
            if not left and not right:
                return True
            # 判断两节点是否其中一个为None，或者两者的值是否不相等
            if not left or not right or left.val != right.val:
                return False
            # 当两个节点值相等时，返回下一层的结果
            return sub(left.left, right.right) and sub(left.right, right.left)
        
        return sub(root.left, root.right) if root else True

    def isSymmetric(self, root: TreeNode) -> bool:
        '''
        借鉴广度搜索方法，目前还存在bug尚未解决
        '''
        if not root:
            return True
        res = [root]
        while res:
            for node in res:
                tmp = res.pop(0)
                if not tmp:
                    res.append(tmp.left)
                    res.append(tmp.right)
            l = len(res)
            if l % 2 != 0:
                return False
            for i in range(l >> 1):
                if res[i] and res[l - 1 - i] and res[i].val == res[l - 1 - i].val:
                    continue
                elif (not res[i]) and (not res[l - 1 - i]):
                    continue
                else:
                    return False
        return True