# 每日打卡 day 1 : 876

'''
链表的中间节点

给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
如果有两个中间结点，则返回第二个中间结点。

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        '''
        双指针法(快慢指针):慢指针每次移动1个节点，快指针每次移动2个节点
        '''
        if not head:
            return None
        if not head.next:
            return head
        slow = head
        fast = head
        # 要同时判断fast和fast.next,因为当fast=None时fast.next无效
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
