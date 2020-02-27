'''
旋转数组的最小元素
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。

输入：[3,4,5,1,2]
输出：1
'''

class Solution:
    def minArray(self, numbers):
        lengh = len(numbers)
        if lengh == 0:
            return 0
        if lengh == 1:
            return numbers[0]
        left = 0 
        right = lengh - 1
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] == numbers[right]:
                right = right - 1
            else:
                right = mid
        return numbers[left]