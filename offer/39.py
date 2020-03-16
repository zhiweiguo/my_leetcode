'''
数组中出现次数超过一半的数字
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        常规思路：先排序，再返回中间位置的元素值
        '''
        nums.sort()
        return nums[len(nums)>>1]

    def majorityElement_2(self, nums: List[int]) -> int:
        '''
        摩尔投票法：
        核心理念为：正负抵消
        票数和： 由于众数出现的次数超过数组长度的一半；若记 众数 的票数为 +1+1 ，非众数 的票数为 -1−1 ，则一定有所有数字的 票数和 > 0>0 。
        票数正负抵消： 设数组 nums 中的众数为 x ，数组长度为 n 。
                      若 nums 的前 a 个数字的 票数和 =0 ，则 数组后 (n−a) 个数字 众数一定仍为 x （即前 a 个数字的票数正负抵消，后 (n-a) 个数字的 票数和仍 >0 ）。

        与target相同，则计数+1，不相等，则-1，最终返回的target的值一定是出现次数超过一半的数
        '''
        # target初始化，计数初始化
        target = nums[0]
        count = 1

        # 遍历
        for i in range(1, len(nums)):
            # 当前位置的元素值与target相等，则计数+1
            if target == nums[i]:
                count += 1
            # 不相等，则计数-1
            else:
                count -=1
            # 当计数为0时，说明抵消完，更换target为当前位置的值
            if count == 0:
                count = 1
                target = nums[i]
        
        return target