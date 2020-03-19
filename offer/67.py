'''
'''

class Solution:
    def strToInt(self, str: str) -> int:
        '''
        先删除左边的空格，再逐位判断
        '''
        str = str.lstrip()
        if len(str) == 0:
            return 0
        # 若第一个元素既不为'-'也不为'+'，而且也不是数字，则直接返回
        if (str[0] != '-' and str[0] != '+') and (not str[0].isdigit()):
            return 0
        flag  = 1 # 符号标志，1位正数，0位负数
        index = 0 # 起始索引初始化
        if str[0] == '-':
            flag = 0
            index = 1
        if str[0] == '+':
            flag = 1
            index = 1
        res = 0
        while index < len(str) and str[index].isdigit():
            res = res * 10 + int(str[index])
            index += 1
        # 边界值处理
        res = min(res, 2**31 - 1) if flag else max(0-res, -2**31)

        return res


