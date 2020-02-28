'''
删除链表的节点

给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        # 判断链表是否为空
        if head is None:  
            return None
        
        # 创建节点，用于指向head
        first = ListNode(0)
        
        # 判断头节点是否为要删除的节点
        if head.val == val:
            first.next = head.next
            return first.next
        first.next = head

        # 遍历链表
        while head.next:
            if head.next.val == val:
                head.next = head.next.next
                break
            head = head.next
        return first.next
