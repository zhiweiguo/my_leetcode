'''
第一个只出现一次的字符

在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。

示例:
s = "abaccdeff"
返回 "b"

'''

class Solution:
    def firstUniqChar(self, s: str) -> str:
        '''
        两步走，第一步遍历统计各个字符出现的次数
        第二步则找到首个次数为1的字符
        '''
        l = len(s)
        if l == 0:
            return ' '
        if l == 1:
            return s
        
        count_dict = {}

        # 遍历字符串，统计各个字符出现的次数到dict中
        for char in s:
            if char in count_dict:
                count_dict[char] = count_dict[char] + 1
            else:
                count_dict[char] = 1
        # 遍历字符串，遇到次数为1的字符就返回，即为答案
        for char in s:
            if count_dict[char] == 1:
                return char
        
        return ' '

    def firstUniqChar_2(self, s):
        '''
        利用python中的接口直接统计各个字符出现的个数
        '''
        import collections
        dic = collections.Counter(s)
        for char in s:
            if dic[char] == 1:
                return char

        return ' '