# 新浪面试原题

'''
两数之和

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        构建一个字典，一次迭代完成构建和查找
        字典中查找的时间复杂度为o(1),所以整体的时间复杂度为o(n)
        这也是该题的最佳解法
        '''

        l = len(nums)
        if l == 0:
            return []
        if l == 1 and nums[0] != target:
            return []
        res = {}
        for i in range(l):
            val = target - nums[i]
            if val in res and res[val] != i:
                return [res[val], i]
            res[nums[i]] = i
        return []
