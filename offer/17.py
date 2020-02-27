'''
打印从1到最大的n位数

输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，
则打印出 1、2、3 一直到最大的 3 位数 999。
'''

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        '''
        法1：两步走，第一步是计算出最大值；第二步是根据最大值来循环添加元素，最终返回列表
        '''
        res = []
        val = 0
        while n > 0:
            val = val * 10 + 9
            n -= 1
        for i in range(1, val+1):
            res.append(i)
        return res

    
    def printNumbers_2(self, n):
        '''
        法2：利用python自带的函数math.pow(x,y) 来得到最大值x的y次幂
        '''
        return [i for i in range(pow(10,n))]  