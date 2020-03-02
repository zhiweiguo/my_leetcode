
# 新浪面试原题
'''
替换空格
把字符串中的空格替换为'%20'

'''

class Solution:
    def replaceSpace(self, s: str) -> str:
        '''
        不是最佳答案
        将字符串转换为list,然后对list中各个元素遍历，若为空格，则替换，最后将list进行拼接为字符串
        '''

        res = list(s)
        for i in range(len(s)):
            if res[i] == ' ':
                res[i] = '%20'
        res = ''.join(res)
        return res

    def replaceSpace(self, s: str) -> str:
        '''
        最佳答案
        创建新的列表，遍历字符串中的每个字符，判断是否为空格进行对应的append，最后在join到一起形成字符串
        '''
        res = []
        for c in s:
            if c == ' ': res.append("%20")
            else: res.append(c)
        return "".join(res)
