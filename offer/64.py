'''
求 1+2+...+n 

要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

'''


class Solution:
    def sumNums(self, n: int) -> int:
        '''
        a and b    解释：当a为真时，返回b的值，当a为假时返回a的值
        因此该法相当于传统递归的变体，时间复杂度很高
        if n == 0:
            return 0
        else:
            return n + self.sumNums(n-1)

        '''
        return n and n + self.sumNums(n - 1)

    def sumNums_2(self, n: int) -> int:
        '''
        同样适用 a and b 的语法判断
        该结果的公式为 n * (n + 1) / 2
        那么可以通过移位的方式迭代实现两数相乘
        3种场景：
            1. b=0,此时不论a为何值，相乘的结果都为0
            2. b=奇数，此时a * b = a * (b - 1) + a;  
            3. b=偶数，此时可以直接调用a * b

        补充说明：
        迭代时让a << 1 ,且b >> 1 有两层含义：
        1. 若b为奇数，需要乘的实际上是a * (b - 1), >>1可以把最低位的1去掉，同时让a << 1, 可以保证结果不变
        2. 让b不断变小，这样b才可以小到0，结束迭代，较少计算次数
        '''
        def muti(a, b):
            return b and (b & 1 and a) + muti(a << 1, b >> 1)  
        return muti(n, n+1) >> 1