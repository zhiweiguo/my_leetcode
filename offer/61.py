'''
扑克牌中的顺子
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。
A 不能视为 14。
'''

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        '''
        不排序，直接比较：
        如果我们能够知道 5 张扑克牌中的最大值 maxValue 和最小值 minValue ，
        那我们就知道，要使它为顺子需要 maxValue - minValue + 1 张牌。
        '''
        flag = [False] * 15
        max_val, min_val = 0, 14
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            if flag[nums[i]]:
                return False
            flag[nums[i]] = True
            max_val = max(max_val, nums[i])
            min_val = min(min_val, nums[i])

        return max_val - min_val <= 4

    def isStraight_2(self, nums: List[int]) -> bool:
        '''
        先排序，再遍历
        '''
        nums.sort()
        zero = 0
        for i in range(len(nums)-1):
            if nums[i] == 0:
                zero += 1
                continue
            if nums[i] == nums[i+1]:
                return False
            # 判断差值，差值为几，则消耗几个0
            zero -= nums[i+1] - nums[i] - 1

        return zero >= 0