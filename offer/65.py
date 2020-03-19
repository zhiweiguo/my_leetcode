'''
不用 + - * / 实现加法运算
'''

class Solution:
    def add(self, a: int, b: int) -> int:
        '''
        原理: a + b = (a ^ b) + ((a & b) << 1)
        再把负数的情况考虑进去即可
        '''
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        while b:
            plus = a ^ b
            b    = ((a & b) << 1) & 0xFFFFFFFF
            a    = plus
        
        return a if a < 0x80000000 else ~(a^0xFFFFFFFF)

# # Java解法：同python，只是不需要额外做异常处理
# class Solution {
#     public int add(int a, int b) {
#         while (b != 0) {
#             int temp = a ^ b;
#             b = (a & b) << 1;
#             a = temp;
#         }
#         return a;
#     }
# }