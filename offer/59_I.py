'''
滑动窗口的最大值

给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

'''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        暴力搜索法：时间复杂度太高
        '''

        if not nums:
            return []
        if len(nums) == 1:
            return nums
        res = []
        for i in range(len(nums)-k+1):
            cur_max = nums[i]
            for j in range(i+1, i+k):
                cur_max = max(cur_max, nums[j])
            res.append(cur_max)

        return res

    def maxSlidingWindow_2(self, nums: List[int], k: int) -> List[int]:
        '''
        优化：
        记录上一个窗口的最大值及索引，判断是否在当前窗口中：
        若在当前窗口中，则只需与当前窗口最后一个值比较，可以减少比较次数，提升效率
        若不在当前窗口中，则比较当前窗口中各个值，找出最大值
        '''
        
        if not nums:
            return []
        if len(nums) == 1:
            return nums
        res = []
        max_index = -1
        max_val = nums[0] 
        for i in range(len(nums)-k+1):
            if max_index >= i and max_index < i+k:
                if max_val < nums[i+k-1]:
                    max_val = nums[i+k-1]
                    max_index = i + k - 1
            else:                
                max_val = nums[i]
                max_index = i
                for j in range(i+1, i+k):
                    if nums[j] >= max_val:
                        max_val = nums[j]
                        max_index = j
            res.append(max_val)

        return res