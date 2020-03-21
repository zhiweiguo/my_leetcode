'''
从上到下打印二叉树
要求：同一层的节点按从左到右的顺序打印，每一层打印到一行。

广度优先遍历
    3
   / \
  9  20
    /  \
   15   7

返回：
[
  [3],
  [9,20],
  [15,7]
]

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        广度优先遍历：
        '''
        res = [] # 保存结果
        if not root:
            return res
        queue = [root]
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
            res.append(tmp)
        
        return res
