'''
包含min函数的栈

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，
调用 min、push 及 pop 的时间复杂度都是 O(1)。

示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.

'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []         # 保存栈元素
        self.min_stack = []     # 保存最小值


    def push(self, x: int) -> None:
        if not self.stack:
            self.min_stack.append(x)       # 若为空，则将当前值放入最小值栈中
        else:
            if self.min_stack[-1] < x:    # 若压栈的值比当前最小值栈最后一个元素大，则将最小值栈最后一个元素再次压栈
                self.min_stack.append(self.min_stack[-1]) 
            else:
                self.min_stack.append(x)
        self.stack.append(x)


    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()


    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return []



    def min(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return []



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()