'''
最小的K个数

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
'''

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        '''
        先排序，再返回前K个数
        '''

        l = len(arr)
        if l < k:
            return None
        if l == k:
            return arr
        arr.sort()
        return arr[:k]

    ded getLeastNumbers_2(self, arr, k):
        '''
        最大堆排序方法：待补充
        '''
