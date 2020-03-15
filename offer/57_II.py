'''
和为s的连续正数序列

例如：
target=9
output: [[2,3,4],[4,5]]

'''

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        '''
        双指针方法实现
        
        '''
        res = []
        left = 1 # 起点
        right = 2 # 终点
        sum_seq = 0

        while left < right:

            # 计算起点到终点的区间和
            sum_seq = ((left + right) * (right - left + 1)) >> 1

            # 若区间和与target相等，则该区间的连续数是一组结果
            if sum_seq == target:
                res.append([num for num in range(left, right + 1)])
                left += 1 # 由于以left为起点的合法解只有一组，所以将left+1,开始判断下一个起点
            
            # 若区间和小于target，则将right+1，扩大区间范围
            elif sum_seq < target:
                right += 1

            # 若区间和大于target，则将left+1，减小区间范围
            else:
                left += 1
        
        return res

    def findContinuousSequence_2(self, target):
        '''
        枚举+暴力搜索法
        '''

        # 待补充