'''
左旋转字符串

字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

示例 1：

输入: s = "abcdefg", k = 2
输出: "cdefgab"

'''

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        '''
        拼接成两个一样的字符串，返回从第n个开始的长度为原始字符串长度的字符串
        '''

        l = len(s)
        s = s + s
        return s[n:l+n]

    def reverseLeftWords_2(self, s, n):
        '''
        切片方式：直接返回
        '''
        return s[n:] + s[:n]

    def reverseLeftWords_3(self, s, n):
        '''
        额外开辟空间，逐个赋值：
        '''
        l = len(s)
        res = ''
        for i in range(n, l+n):
            res += s[i % l]

        return res
