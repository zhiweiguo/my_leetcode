'''
连续子数组的最大和

输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。
求所有子数组的和的最大值。要求时间复杂度为O(n)。

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        动态规划：
        遍历数组，判断该位置元素是否可以组成最大和的连续子数组的依据就是看之前的元素和是否为正数
        
        return: 最大值

        '''

        l = len(nums)
        if l == 0:
            return None
        if l == 1:
            return nums[0]
        # 对当前最大值以及最终的最大值赋初值
        max_sum = nums[0]
        cur_sum = nums[0]
        for i in range(1, l):
            # 若cur_sum > 0， 则可以将该位置的值与cur_sum求和
            cur_sum = cur_sum + nums[i] if cur_sum > 0 else nums[i]
            # 更新全局最大值
            max_sum = max(max_sum, cur_sum)
        
        return max_sum