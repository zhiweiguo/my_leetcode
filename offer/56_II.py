'''
数组中数字出现的次数
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

示例 1：
输入：nums = [3,4,3,3]
输出：4
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        构建字典，当某个num的计数值达到3个时，删除该键值对
        '''
        if len(nums) == 1:
            return nums[0]
        count_dict = {}
        for num in nums:
            if num not in count_dict:
                count_dict[num] = 1
            else:
                if count_dict[num] == 2:
                    del count_dict[num]
                else:
                    count_dict[num] += 1

        #for key, val in count_dict.items():
        #    if val == 1:
        #        return key

        return list(count_dict.keys())[0]

    def singleNumber_2(self, nums: List[int]) -> int:
        '''
        先排序，再遍历判断，i位置的元素与i-1和i+1位置的元素均不相等时则为答案
        '''

        
