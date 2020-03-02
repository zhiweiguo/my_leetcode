# 新浪面试原题

'''
二分查找

给定一个排好序的数组和一个目标值target，搜索出目标值对应的索引，若没有，则返回-1

'''


def binary_search(arr, val):
    l = len(arr)
    if l == 0:
        return -1

    if l == 1 and val != arr[0]:
        return -1
    left = 0
    right = l - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == val:
            return mid
        if val >= arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1