# 每日打卡 day8 : offer 62

'''
圆圈中最后剩下的数字
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。
求出这个圆圈里剩下的最后一个数字。

例如：
0、1、2、3、4这5个数字组成一个圆圈，
从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，
因此最后剩下的数字是3。
'''

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        '''
        构建数组，计算索引依次删除，时间复杂度较高，待优化
        '''
        num = [i for i in range(n)]
        # 起始索引初始化
        start = 0
        # 长度>1，则一直循环
        while len(num) > 1:
            # 计算待删除元素索引
            idx = (start + m - 1) % len(num)
            # 删除该索引元素
            num.pop(idx)
            # 更新起始索引为删除元素位置
            start = idx
        
        return num[0]

    def lastRemaining_2(self, n: int, m: int) -> int:
        '''
        数学+递归
        '''
        def f(n, m):
            if n == 1:
                return 0
            x = f(n-1, m)

            return (m+x) % n

        return f(n, m)

    def lastRemaining_3(self, n: int, m: int) -> int:
        '''
        数学+迭代：基于方法2优化而来，节省了空间
        '''
        x = 0
        for i in range(2, n+1):
            x = (m+x) % i
        
        return x

