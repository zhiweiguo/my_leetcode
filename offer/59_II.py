'''
队列的最大值
请定义一个队列并实现函数 max_value 得到队列里的最大值，
要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
'''

class MaxQueue:

    def __init__(self):
        # 之所以使用deque而不使用list，是因为deque的pop(i)是o(1)时间复杂度，而list是o(n)
        from collections import deque
        self.queue = deque()      # 原始队列
        self.max_queue = deque()  # 辅助队列，记录当前队列的最大值，递减队列


    def max_value(self) -> int:
        # 因为头部记录当前队列最大值，因此直接返回第一个位置的元素
        return self.max_queue[0] if self.max_queue else -1

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        # 保证max_queue的头部总是原始队列queue的最大值
        # 删除max_queue中小于value的元素
        while self.max_queue and self.max_queue[-1] < value:
            self.max_queue.pop()
        self.max_queue.append(value)

    def pop_front(self) -> int:
        if self.queue:
            # popleft即pop左边第一个元素，相当于pop(0)
            res = self.queue.popleft()
            # 如果当前要pop的元素值与max_queue的第一个值相等，那么也将其第一个值pop
            if res == self.max_queue[0]:
                self.max_queue.popleft()
            return res
        else:
            return -1



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()