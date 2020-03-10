'''
0 ~ n-1中的缺失值

一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        常规思路：遍历，判断当前元素与上一个元素差值是否为1，若不为1，则返回当前索引即为结果

        '''
        # 只有一个元素的情况判断
        if len(nums) == 1:
            return 1 if nums[0] == 0 else 0

        # 若第1个元素不为0，则可以直接返回
        if nums[0] != 0:
            return 0

        # 遍历
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                return i

        # 执行到此，则说明前面元素都连续，返回最后的元素
        return len(nums)

    def missingNumber_2(self, nums):
        '''
        二分查找
        '''
        # 初始化左右索引
        left, right = 0, len(nums)
        while left < right:
            # 求中间索引
            mid = left+(right-left) >> 2
            
            # 当中间元素的值==索引时，说明前半段数据连续，否则后半段数据连续
            if nums[mid]==mid: 
                left = mid+1
            else: 
                right = mid

        return(left)
