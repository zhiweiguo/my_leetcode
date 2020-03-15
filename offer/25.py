'''
合并两个排序的链表

输入两个递增排序的链表，合并两个链表，并使新链表中的节点仍然是递增排序的

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # 定义伪头节点
        first = head = ListNode(0)

        # 当l1 或 l2 为空时跳出循环
        while l1 and l2:
            # 判断节点值大小，并更新各自指向
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        
        # 将非空的节点连接到新链表尾部
        head.next = l2 if l2 else l1
        
        return first.next
            

