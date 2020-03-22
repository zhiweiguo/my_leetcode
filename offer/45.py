'''
把数组排成最小的数

输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
打印能拼接出的所有数字中最小的一个。

示例 2:

输入: [3,30,34,5,9]
输出: "3033459"

'''

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        '''
        先把数组中各个元素转为字符串类型
        再对各个字符串进行相加的结果比较
        '''
        if not nums:
            return ""
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) > (nums[j] + nums[i]):
                    nums[i], nums[j] = nums[j], nums[i]
        
        return ''.join(nums)