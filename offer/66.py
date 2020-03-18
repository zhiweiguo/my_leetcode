'''
构建乘积数组
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，
其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。
不能使用除法。

输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
'''

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        '''
        创建双数组，对称遍历
        '''
        if not a:
            return []
        length = len(a)
        #if length == 1:
        #    return a 
        left = [1] * length
        right = [1] * length
        res = []
        for i in range(1, length-1):
            left[i] = left[i-1] * a[i-1]
            right[length-1-i] = right[length-i] * a[length-i]
        # 边界位置赋值
        left[length-1] = left[length-2] * a[length-2]
        right[0] = right[1] * a[1]
        
        for i in range(length):
            res.append(left[i] * right[i])
        
        return res