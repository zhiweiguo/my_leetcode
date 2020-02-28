'''
链表中倒数第K个节点

输入一个链表，输出该链表中倒数第k个节点。
为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def __init__(self):
        self.pos = 0

    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        '''
        采用快慢指针的方式实现
        return: 倒数第K个节点
        '''
        # 定义快慢指针的起始位置
        slow = head
        fast = head
        # 让快指针首先遍历到第K个节点
        n = 1
        while n < k:
            if fast:
                fast = fast.next
                n += 1
            else:
                return None
        # 快慢指针同时开始遍历，直到快指针访问到最后一个节点停止
        while fast.next:
            fast = fast.next
            slow = slow.next
        return slow

    def getKthFromEnd_1(self, head: ListNode, k: int) -> ListNode:
        '''
        采用快慢指针的方式实现:整合到一个循环中
        return: 倒数第K个节点
        '''
        # 定义快慢指针的起始位置
        slow = head
        fast = head
        # 快指针遍历，直到快指针访问到最后一个节点停止
        while fast:
            fast = fast.next
            
            if k == 0:  # 说明快指针已经移动了K次，此时满指针开始移动
                slow = slow.next
            else:       # 说明满指针尚未移动够K次，此时k-1
                k -= 1
        return slow

    def getKthFromEnd_2(self, head, k):
        '''
        递归方式实现:
        1. 先一直递归到链表尾部，再返回
        2. 定义位置变量 pos ，每次函数返回时 pos++
        3. 当 pos == k 时，说明此时递归函数位于第 k 个结点位置，返回该结点

        '''
        if not head:
            return None
        node = self.getKthFromEnd_2(head.next, k)
        self.pos += 1
        if self.pos == k:
            return head
        
        return node
