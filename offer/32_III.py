'''
请实现一个函数按照之字形顺序打印二叉树，
即第一行按照从左到右的顺序打印，
第二层按照从右到左的顺序打印，
第三行再按照从左到右的顺序打印，其他行以此类推。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = [] # 保存结果
        if not root:
            return res
        queue = [root]
        flag = 1
        while queue:
            tmp = []
            # 每次的for循环相当于遍历一层
            for i in range(len(queue)):
                node = queue.pop(0) # 弹出第一个节点
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left) # 将左节点添加到队列尾部
                if node.right:
                    queue.append(node.right) # 将右节点添加到队列尾部

            res.append(tmp[::-1] if len(res) % 2 else tmp)
        
        return res