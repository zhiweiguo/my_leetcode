'''
和为S的两个数字

输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。
如果有多对数字的和等于s，则输出任意一对即可。

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        法1：字典

        '''
        res_dic = {}
        res_dic[target - nums[0]] = 0
        for i in range(1, len(nums)):
            if nums[i] in res_dic:
                return [target - nums[i], nums[i]]
            else:
                res_dic[target - nums[i]] = i
        
        return []
    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        '''
        法2: 基于法1优化，使用set

        '''
        visited = set()
        for num in nums:
            if target - num in visited:
                return [num, target - num]
            visited.add(num)
        return []

    def twoSum_3(self, nums: List[int], target: int) -> List[int]:
        '''
        法3：双指针
        
        '''
        left, right = 0, len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                return [nums[left], nums[right]]

            if s > target:
                right -= 1
            else:
                left += 1
        
        return []



