'''
反转链表

定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        双指针方法：
        定义两个指针： pre 和 cur ；pre 在前 cur 在后。
        每次让 pre 的 next 指向 cur ，实现一次局部反转
        局部反转完成之后， pre 和 cur 同时往前移动一个位置
        循环上述过程，直至 pre 到达链表尾部
        return: 新链表的头节点
        '''
        # 判断链表是否为空
        if not head:
            return None
        # 定义新链表头节点，首先赋值为None，作为末尾节点的next使用
        first = None
        # 依次遍历原链表中的节点
        while head:
            tmp = head.next    # 暂存原链表的next, 下一次遍历使用
            head.next = first  # 将当前新链表的头节点链接到当前head的next,实现局部反转
            first = head       # 更新反转后链表的头节点
            head = tmp         # 将原链表的next用于下次遍历
        return first

    def reverseList_2(self, head):
        '''
        递归方式：待补充
        '''
        return