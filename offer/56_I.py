'''
数组中数字出现的次数
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。
请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

示例 1：

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
'''

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        l = len(nums)
        if l < 2:
            return []
        res = []
        nums.sort()
        if nums[0] != nums[1]:
            res.append(nums[0])
        if nums[l-1] != nums[l-2]:
            res.append(nums[l-1])
        for i in range(1, l-1):
            if (nums[i] != nums[i-1]) and (nums[i] != nums[i+1]):
                res.append(nums[i])
            if len(res) == 2:
                return res

        return res