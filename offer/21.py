'''
调整数组顺序使奇数位于偶数前面

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
 
示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。

'''

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        '''
        法1：双指针，left从左往右，right从右往左
        '''
        l = len(nums)
        if l == 0:
            return []
        if l == 1:
            return nums
        left = 0
        right = l - 1
        while left < right:
            while left < l-1 and nums[left] % 2 != 0:
                left += 1
            while right > -1 and nums[right] % 2 == 0:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
            left  += 1
            right -= 1
        return nums

    def exchange_2(self, nums):
        '''
        法2： 快慢指针，快指针遇到奇数，则与满指针位置的元素交换，满指针+1
        '''
        l = len(nums)
        if l == 0:
            return []
        if l == 1:
            return nums
        slow = 0
        fast = 0
        while fast < l:
            if nums[fast] % 2 == 1:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1

        return nums







