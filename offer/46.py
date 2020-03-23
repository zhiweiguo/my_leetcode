'''
把数字翻译成字符串

给定一个数字，我们按照如下规则把它翻译为字符串：
0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

'''

class Solution:
    def translateNum(self, num: int) -> int:
        '''
        这道题其实就是一个递归：
        递归出口是num是只有一位数，以xyzcba为例，先取最后两位（个位和十位）即ba，
        如果ba>=26，必然不能分解成f(xyzcb)+f(xyzc)，此时只能分解成f(xyzcb);
        但还有一种情况，就是ba<=9,也就是该数十位上为0，此时也不能分解。
        '''
        if num <= 9:
            return 1
        val = num % 100
        if val >= 26 or val <= 9:
            return self.translateNum(num//10)
        else:
            return self.translateNum(num//10) + self.translateNum(num//100)